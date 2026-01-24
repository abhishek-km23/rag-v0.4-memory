from langchain_huggingface import HuggingFaceEmbeddings


def load_embeddings():
    """
    Load HuggingFace sentence embeddings.
    Single source of truth for embedding configuration.
    Used by vector store and retriever.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
