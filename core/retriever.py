from typing import List
from langchain_core.documents import Document
from core.vector_store import get_retriever


def retrieve_documents(query: str, k: int = 4) -> List[Document]:
    """
    Retrieve top-k relevant documents for a query.

    Steps:
    1. Load persistent vector store.
    2. Perform similarity search.
    3. Return documents with metadata intact.
    """
    retriever = get_retriever(k=k)
    return retriever.invoke(query)
