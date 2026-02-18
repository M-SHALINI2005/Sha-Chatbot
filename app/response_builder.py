def build_response(question, books, model):

    prompt = f"""
User asked: {question}

Books data:
{books}

Write a helpful natural reply for the user.
"""

    res = model.generate_content(prompt)

    return {
        "response": res.text,
        "metadata": books
    }
