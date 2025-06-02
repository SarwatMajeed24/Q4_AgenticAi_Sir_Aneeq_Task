## 🛠️ Installation

### On Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### On Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 🧪 Create a Python Project Using `uv`

### 1. Initialize a project

```bash
uv init
```

This generates a `pyproject.toml` file.

### 2. Add dependencies

```bash
uv add flask
```

This will create or update a `uv.lock` file.

### 3. Create a virtual environment

```bash
uv venv
```

### 4. Run your script

```bash
uv run app.py
```

---

## 📁 Example `README.md`

````markdown
# Fast Python Project using `uv`

## 🚀 About

This project uses [`uv`](https://astral.sh/docs/uv) – a high-performance Python package manager – for dependency and project management.

## 🔧 Setup

### Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
````

### Initialize Project

```bash
uv init
uv add requests rich
uv lock
uv venv
```

### Run the App (example)

```bash
uv run app.py      
```