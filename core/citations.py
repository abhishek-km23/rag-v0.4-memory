from typing import List
from langchain_core.documents import Document


def format_citations(docs: List[Document]) -> str:
    """
    Formats citation information from retrieved documents.

    Steps:
    1. Iterate over retrieved chunks.
    2. Extract source, page, and chunk_id metadata.
    3. Attach a short text snippet.
    """
    citations = []

    for idx, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        snippet = doc.page_content[:200].replace("\n", " ")

        citations.append(
            f"[{idx}] source: {source} | page: {page} | chunk_id: {chunk_id}\n"
            f"    \"{snippet}...\""
        )

    return citations
