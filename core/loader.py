'''
Docstring for v0.3.core.loader
    This file is responsible for:
        Validate that the PDF file exists at the given path.
        Load the PDF using a page-aware PDF loader.
        Extract text page by page.
        Create one Document object per page.
        Attach the PDF filename as source metadata.
        Preserve the page number in metadata.
        Return the list of page-level Document objects.
'''

from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
import os


def load_pdf(pdf_path: str) -> List[Document]:
    """
    Loads a PDF and returns Documents with page metadata.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    filename = os.path.basename(pdf_path)

    for d in docs:
        d.metadata["source"] = filename
        d.metadata["page"] = d.metadata.get("page", None)

    return docs
