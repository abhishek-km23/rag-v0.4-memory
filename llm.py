from langchain_ollama import OllamaLLM


def load_llm():
    """
    Load Ollama LLM using CPU only.
    """
    return OllamaLLM(
        model="llama3",
        temperature=0.0,
        num_gpu=0,
        streaming=False
    )
