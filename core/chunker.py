'''
Docstring for v0.3.core.chunker
    This file is responsible for:
        Accept a list of page-level Document objects.
        Split each document into overlapping text chunks.
        Ensure chunks remain semantically coherent.
        Assign a unique chunk_id to every chunk.
        Preserve original metadata (source, page) in each chunk.
        Return the list of chunked Document objects.
'''

import hashlib
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import uuid


def chunk_documents(
    docs: List[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 150,
    ) -> List[Document]:
    """
    Splits documents into chunks and assigns stable citation metadata.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = splitter.split_documents(docs)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"{chunk.metadata.get('source', 'doc')}__{chunk.metadata.get('page', -1)}__{i}"
        chunk.metadata["embedding_key"] = hashlib.sha256(chunk.page_content.encode("utf-8")).hexdigest()


    return chunks
