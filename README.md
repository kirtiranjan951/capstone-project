# RAG-Bank-Testing — Minimal CLI Prototype

A minimal Retrieval-Augmented Generation (RAG) prototype for a banking assistant. The application builds an embeddings index from local text documents and answers user questions using relevant retrieved context.

## Features

- Build a searchable embeddings index from local text files.
- Retrieve relevant context for user questions.
- Generate answers using OpenAI embeddings and chat completions.
- Provide a simple command-line interface (CLI).

## Prerequisites

- Python 3.8 or later
- An OpenAI API key
- Pip package manager

## Project Structure

```text
RAG-Bank-Testing/
├── app/
│   ├── __init__.py
│   ├── rag_cli.py
│   └── index.pkl
├── documents/
├── docs/
├── reports/
├── requirements.txt
└── README.md
```

*Note: The project structure above is illustrative. Adjust it to match your actual files.*

## Installation

1. Clone the repository and navigate to the project directory.

   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd RAG-Bank-Testing
   ```

2. Create and activate a virtual environment.

   **Windows PowerShell:**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set your OpenAI API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="your-openai-api-key"
```

**macOS/Linux:**

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

Replace the placeholder with your actual API key. Never commit API keys or other secrets to version control.

## Usage

### 1. Build the embeddings index

The CLI reads `.txt` files from the `documents/`, `docs/`, and `reports/` directories by default.

```bash
python -m app.rag_cli build
```

### 2. Ask a question

For example, ask about the loan approval process:

```bash
python -m app.rag_cli ask "What is the loan approval process?"
```

The application retrieves relevant document context and uses the configured OpenAI models to generate an answer.

## Index Storage

The generated index is stored at:

```text
app/index.pkl
```

Build or regenerate the index when the source documents change.

## Important Notes

- This prototype uses OpenAI embeddings and chat completions.
- API access requires a valid OpenAI API key and sufficient API quota.
- The commands assume that `app/rag_cli.py` and its CLI entry points are implemented as described.
- Only use documents you are authorized to access.
- Avoid committing generated indexes if they contain sensitive banking information.

## Troubleshooting

**ModuleNotFoundError: No module named 'app'**

Run commands from the project root directory, where the `app/` package is located. Ensure that `app/__init__.py` exists.

**OpenAI authentication errors**

Verify that `OPENAI_API_KEY` is set correctly in the terminal running the application.

**No documents found**

Ensure that your `.txt` files are placed inside one of the configured input directories.

## License

Add the appropriate license information before distributing this project.
