from llm import load_llm
from core.qa import answer_question


def qa_loop():
    """
    Interactive Question–Answer loop.
    Uses persistent vector store and returns answers with citations.
    """
    print("\n[INFO] Q/A started. Type 'exit' to quit.\n")

    llm = load_llm()

    while True:
        question = input("Ask a question: ").strip()

        if question.lower() == "exit":
            print("[INFO] Exiting Q/A.")
            break

        try:
            answer, citations = answer_question(question, llm)

            print("\nAnswer:")
            print(answer)

            print("\nCitations:")
            for cite in citations:
                print(cite)

        except Exception as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    qa_loop()
