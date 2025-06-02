# import os
# from dotenv import load_dotenv
# import chainlit as cl
# from litellm import completion
# import json

# # Load the environment variables from the .env file
# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Check if the API key is present; if not, raise an error
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# @cl.on_chat_start
# async def start():
#     """Set up the chat session when a user connects."""
#     # Initialize an empty chat history in the session.
#     cl.user_session.set("chat_history", [])

#     await cl.Message(content="Welcome to the Panaversity AI Assistant! How can I help you today?").send()

# @cl.on_message
# async def main(message: cl.Message):
#     """Process incoming messages and generate responses."""
#     # Send a thinking message
#     msg = cl.Message(content="Thinking...")
#     await msg.send()

#     # Retrieve the chat history from the session.
#     history = cl.user_session.get("chat_history") or []
    
#     # Append the user's message to the history.
#     history.append({"role": "user", "content": message.content})
    

#     try:
#         # Get completion from LiteLLM
#         response = completion(
#             model="gemini/gemini-2.0-flash",
#             api_key=gemini_api_key,
#             messages=history
#         )
        
#         response_content = response.choices[0].message.content
        
#         # Update the thinking message with the actual response
#         msg.content = response_content
#         await msg.update()

#         # Append the assistant's response to the history.
#         history.append({"role": "assistant", "content": response_content})
    
#         # Update the session with the new history.
#         cl.user_session.set("chat_history", history)
        
#         # Optional: Log the interaction
#         print(f"User: {message.content}")
#         print(f"Assistant: {response_content}")
        
#     except Exception as e:
#         msg.content = f"Error: {str(e)}"
#         await msg.update()
#         print(f"Error: {str(e)}")


# # Right on it is not fully functioning because we are not
# # loading json file on on_chat_start
# @cl.on_chat_end
# async def on_chat_end():
#     # Retrieve the full chat history at the end of the session
#     history = cl.user_session.get("chat_history") or []
#     # Save the chat history to a file (or persist it elsewhere)
#     with open("chat_history.json", "w") as f:
#         json.dump(history, f, indent=2)
#     print("Chat history saved.")

import os
import json
import time
import asyncio
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Welcome to the Panaversity AI Assistant! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses with retry logic."""
    msg = cl.Message(content="Thinking...")
    await msg.send()

    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds

    response_content = None

    for attempt in range(MAX_RETRIES):
        try:
            response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=gemini_api_key,
                messages=history
            )
            response_content = response.choices[0].message.content
            break  # Exit loop on success
        except Exception as e:
            if "503" in str(e) and attempt < MAX_RETRIES - 1:
                await msg.stream_token(f"\nModel busy, retrying... ({attempt + 1}/{MAX_RETRIES})")
                await asyncio.sleep(RETRY_DELAY)
            else:
                error_msg = "The AI model is temporarily overloaded. Please try again in a few minutes."
                msg.content = f"Error: {error_msg}"
                await msg.update()
                print(f"Error: {str(e)}")
                return

    if response_content:
        msg.content = response_content
        await msg.update()
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

@cl.on_chat_end
async def on_chat_end():
    """Save the chat history at the end of the session."""
    history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved.")
