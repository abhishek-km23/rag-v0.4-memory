# RAG v0.3 — Multi-PDF Persistent RAG with Citations (Offline)

This project implements a **fully offline Retrieval-Augmented Generation (RAG) system**
that supports **multiple PDFs**, **persistent vector storage**, and **citation-backed answers**.

The system is designed with **clear separation of concerns**:
- one entry point for document ingestion
- one entry point for question answering

No external APIs are required.

---

## Key Features

- Multi-PDF incremental ingestion
- Persistent FAISS vector store (disk-backed)
- HuggingFace sentence embeddings (free, local)
- Local LLM inference using Ollama
- Citation-backed answers (source, page number, chunk ID)
- Fully offline and cost-free
- Resume- and interview-ready architecture

---

## Architecture Overview

PDFs → Loader → Chunker → Embeddings → FAISS (persistent)
↓
Retriever
↓
Local LLM
↓
Answer + Citations


- **Ingestion** and **Q/A** are handled via separate entry points.
- Embeddings are created once and reused across sessions.

---

## Project Structure
```
.
├── main_ingest.py        # PDF ingestion (write path)
├── main_qa.py            # Question answering (read path)
├── llm.py                # Local Ollama LLM loader
│
├── core/
│   ├── __init__.py       # Marks core as a Python package
│   ├── loader.py         # PDF loading + page metadata
│   ├── chunker.py        # Text chunking + chunk_id metadata
│   ├── embeddings.py    # HuggingFace embeddings configuration
│   ├── vector_store.py  # FAISS create / load / append / persist
│   ├── retriever.py     # Similarity retrieval logic
│   ├── citations.py     # Citation formatting
│   └── qa.py             # Answer generation helper (LLM + context)
│
├── data/                 # PDFs (ignored by git)
├── vector_store/         # FAISS index (ignored by git)
├── .gitignore
└── README.md

```
---

## How to Run

### 1. Ingest PDFs
Place PDF files inside the `data/` directory, then run:

```bash
python main_ingest.py

This creates or updates the persistent FAISS vector store.

```

### 2. Ask Questions
python main_qa.py

- Ask questions related to the ingested documents.
- Each answer is returned with citations.

### Tech Stack

- Python
- LangChain (modular packages)
- FAISS
- HuggingFace sentence-transformers
- Ollama (local LLM)

### Notes

- No OpenAI or paid APIs are used.
- Works fully offline.
- Designed to demonstrate real-world RAG system design.