'''
Docstring for v0.3.core.vector_store
    This file is responsible for:
        loading an existing FAISS index (if present)
        creating it if missing
        appending new documents
        persisting to disk

    Assumptions:
        Embeddings: HuggingFace (HuggingFaceEmbeddings)
        Vector store: FAISS
        Persistence path: v0.3/vector_store/
'''

import os
from typing import List

from langchain_community.vectorstores import FAISS
from core.embeddings import load_embeddings
from langchain_core.documents import Document


VECTOR_STORE_DIR = "vector_store"
INDEX_FILE = os.path.join(VECTOR_STORE_DIR, "index.faiss")


def load_vector_store() -> FAISS:
    """
    Load FAISS vector store from disk if it exists,
    otherwise create a new empty one.
    """
    embeddings = load_embeddings()


    if not os.path.exists(INDEX_FILE):
        raise RuntimeError(
            "Vector store does not exist. Run ingestion first."
        )

    return FAISS.load_local(
        VECTOR_STORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )


def add_documents(docs: List[Document]) -> None:
    """
    Add new documents to the persistent vector store.
    """
    if not docs:
        return
    
    embeddings = load_embeddings()

    # First-time creation
    if not os.path.exists(INDEX_FILE):
        vector_store = FAISS.from_documents(docs, embeddings)
    else:
        vector_store = FAISS.load_local(
            VECTOR_STORE_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )
        vector_store.add_documents(docs)

    vector_store.save_local(VECTOR_STORE_DIR)


def get_retriever(k: int = 4):
    """
    Returns a retriever for Q/A.
    Read-only usage in main_qa.py.
    """
    vector_store = load_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": k})
