from core.retriever import retrieve_documents
from core.citations import format_citations
from llm import load_llm


def qa_loop():
    """
    Q/A loop using persistent vector store and citation-backed answers.

    Steps:
    1. Load local LLM.
    2. Accept user questions.
    3. Retrieve relevant chunks.
    4. Generate answer from retrieved context.
    5. Display answer with citations.
    """
    llm = load_llm()

    print("\n[INFO] Q/A started. Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ").strip()

        if question.lower() == "exit":
            print("[INFO] Exiting Q/A.")
            break

        docs = retrieve_documents(question)

        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
                    Use the following context to answer the question.
                    Do not make up information.

                    Context:
                    {context}

                    Question:
                    {question}
        """

        answer = llm.invoke(prompt)

        print("\nAnswer:")
        print(answer)

        print("\nCitations:")
        print(format_citations(docs))
        print("-" * 50)


if __name__ == "__main__":
    qa_loop()
