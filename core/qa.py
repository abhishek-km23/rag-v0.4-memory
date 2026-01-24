from core.retriever import get_retriever
from core.citations import format_citations


def answer_question(question: str, llm, k: int = 4):
    """
    Retrieve relevant documents and generate
    an answer with citations.
    """
    retriever = get_retriever(k=k)
    docs = retriever.invoke(question)

    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
                Use the context below to answer the question.
                Cite sources explicitly.

                Context:
                {context}

                Question:
                {question}
            """

    answer = llm.invoke(prompt)
    citations = format_citations(docs)

    return answer, citations
