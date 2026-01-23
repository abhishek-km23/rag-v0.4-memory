import os
from core.loader import load_pdf
from core.chunker import chunk_documents
from core.vector_store import add_documents


DATA_DIR = "data"


def ingest_pdfs():
    """
    Ingests all PDFs found in the data directory into the persistent vector store.

    Steps:
    1. Scan the data directory for PDF files.
    2. Load each PDF page-wise with metadata.
    3. Chunk the documents while preserving metadata.
    4. Add chunks to the persistent FAISS vector store.
    """
    
    if not os.path.exists(DATA_DIR):
        print(f"[INFO] Data directory '{DATA_DIR}' does not exist.")
        return

    pdf_files = [
        os.path.join(DATA_DIR, f)
        for f in os.listdir(DATA_DIR)
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("[INFO] No PDF files found to ingest.")
        return

    all_chunks = []

    for pdf_path in pdf_files:
        print(f"[INFO] Ingesting: {pdf_path}")
        docs = load_pdf(pdf_path)
        chunks = chunk_documents(docs)
        all_chunks.extend(chunks)

    add_documents(all_chunks)
    print("[INFO] Ingestion completed successfully.")


if __name__ == "__main__":
    ingest_pdfs()
