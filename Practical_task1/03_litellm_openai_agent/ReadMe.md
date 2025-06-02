## 🧠 What is LiteLLM?

**[LiteLLM](https://github.com/BerriAI/litellm)** is a Python package that provides a **unified interface** to call multiple Large Language Models (LLMs) from different providers like:

* OpenAI (e.g., GPT-3.5, GPT-4)
* Google (Gemini / PaLM via VertexAI)
* Anthropic (Claude)
* Mistral, Cohere, HuggingFace, and others

### 🔧 Why use LiteLLM?

* ✅ **One standard API** for all major LLM providers
* 🔄 **Easy to switch** between models (just change the model name)
* 🔐 **Environment-based API key handling**
* 🔁 Built-in support for **retry logic**, **streaming**, and **chat history**
* 🧩 Compatible with frameworks like **LangChain** and **Chainlit**


## 📄 README.md (You Can Copy This)

````markdown
# Panaversity AI Assistant 🤖

A conversational AI chatbot powered by **Chainlit** and **LiteLLM**, using Google's Gemini API. Built for educational use, this assistant supports user interactions and maintains chat history in a JSON file.


## 🚀 Features

- Chat interface via [Chainlit](https://www.chainlit.io/)
- LLM backend via [LiteLLM](https://github.com/BerriAI/litellm)
- Supports Google's Gemini 2.0 Flash model
- Maintains and saves chat history
- Retry logic for model overload (503 errors)
- Simple `.env`-based API key management


## 🛠️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install chainlit litellm python-dotenv
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory with:

```
GEMINI_API_KEY=your_google_vertex_ai_key_here
```

## 🧪 Run the Chatbot

```bash
chainlit run main.py
```

Then open your browser to: [http://localhost:8000](http://localhost:8000)


## 📦 Project Structure

```
.
├── main.py                # Chainlit app using LiteLLM
├── .env                   # Your Gemini API key
├── chat_history.json      # Saved chat logs
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```


## ⚠️ Error Handling

If you encounter a `503 Model Overloaded` error from Gemini, the app will:

* Retry the request up to 3 times
* Gracefully inform the user if the model is still unavailable


## 🧩 About LiteLLM

LiteLLM provides a standard `.completion()` and `.chat_completion()` API to unify access to multiple LLM providers. In this project, it connects to:

* `gemini/gemini-2.0-flash` via Vertex AI
* Additional models (e.g., OpenAI GPT-3.5) can be swapped in easily

