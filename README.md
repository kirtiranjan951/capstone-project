# RAG-Bank-Testing — Minimal CLI prototype

This is a minimal Retrieval-Augmented Generation (RAG) prototype for a bank assistant. It provides a simple CLI to build an embeddings index from local text files and to ask questions using retrieved context.

Prerequisites:
- Python 3.8+
- `OPENAI_API_KEY` environment variable set

Install:

```bash
pip install -r requirements.txt
```

Usage:

Build the index (reads `.txt` files under `documents/`, `docs/`, and `reports/` by default):

```bash
python -m app.rag_cli build
```

Ask a question:

```bash
python -m app.rag_cli ask "What is the loan approval process?"
```

Notes:
- This prototype uses OpenAI embeddings and chat completions.
- The index is stored at `app/index.pkl`.
