from ollama import chat

from config.settings import MODEL_NAME
from app.memory.parser import parse_json


def extract_memory(text: str, mode="save"):

    if mode == "save":

        prompt = f"""
You are an AI memory extraction system.

Your task is to extract long-term memory from the user's sentence.

Rules:

1. Return ONLY valid JSON.
2. Do NOT write explanations.
3. Do NOT use markdown.
4. Do NOT use ```json.
5. If no memory is found return:

{{
    "memory_type": "",
    "attribute": "",
    "value": ""
}}

Examples:

Input:
Remember that my favorite language is Python.

Output:
{{
    "memory_type": "preference",
    "attribute": "favorite_language",
    "value": "Python"
}}

Input:
My birthday is 12 March.

Output:
{{
    "memory_type": "personal_info",
    "attribute": "birthday",
    "value": "12 March"
}}

Now extract memory.

Sentence:
{text}
"""

    else:

        prompt = f"""
You are an AI memory recall extractor.

Return ONLY valid JSON.

Rules:

1. Return only JSON.
2. No explanation.
3. No markdown.

If you cannot identify the attribute, return:

{{
    "attribute": ""
}}

Examples:

Input:
What is my favorite fruit?

Output:
{{
    "attribute": "favorite_fruit"
}}

Input:
What is my favorite language?

Output:
{{
    "attribute": "favorite_language"
}}

Input:
What is my name?

Output:
{{
    "attribute": "name"
}}

Input:
Where do I live?

Output:
{{
    "attribute": "city"
}}

Sentence:
{text}
"""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    result = response["message"]["content"]

    return parse_json(result)