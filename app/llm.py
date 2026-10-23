import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:3b"


def generate_answer(question: str, context: str) -> str:
    """Generate a grounded answer using retrieved document context."""

    system_prompt = """
You are a careful AI research assistant that answers questions
about documents.

Follow these rules strictly:

1. Use only the information explicitly provided in the document context.
2. Answer the exact question asked. Do not answer a different question.
3. Identify the type of information requested before answering.
4. Keep different categories of information separate.
   For example, exam subjects are different from university degree programs.
5. Do not include degree programs when the user asks for exam subjects.
6. Do not combine information from unrelated sections unless the question
   explicitly asks for a comparison or summary.
7. Do not invent facts or add unsupported details.
8. If the context does not contain enough information, clearly say so.
9. Prefer a concise, direct answer over a long, repetitive explanation.
10. Answer in Turkish, even if the question is written in English.
11. Preserve the meaning of the original document.
12. If the context contains a relevant page number, include it as a source
    reference when possible.

Before answering, silently check that every claim is supported by
the provided context and directly relevant to the question.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt.strip(),
        },
        {
            "role": "user",
            "content": (
                f"DOCUMENT CONTEXT:\n{context}\n\n"
                f"QUESTION:\n{question}\n\n"
                "Provide a concise answer based only on the context."
            ),
        },
    ]

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                },
            },
            timeout=180,
        )

        response.raise_for_status()

        result = response.json()

        message = result.get("message", {})
        answer = message.get("content", "")

        if not isinstance(answer, str) or not answer.strip():
            raise RuntimeError(
                "Ollama returned an empty or invalid answer."
            )

        return answer.strip()

    except requests.RequestException as error:
        raise RuntimeError(
            f"Could not communicate with Ollama: {error}"
        ) from error