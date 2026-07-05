from ollama import chat

from config.settings import MODEL_NAME
from app.memory.parser import parse_json


def extract_memory(text: str, mode="save"):

    # ---------------- SAVE ----------------

    if mode == "save":

        prompt = f"""
You are an AI memory extraction system.

Your task is to extract long-term memory from the user's sentence.

Rules:

1. Return ONLY valid JSON.
2. Do NOT write explanations.
3. Do NOT use markdown.
4. Do NOT use ```json.

If no memory is found return:

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

Sentence:
{text}
"""

    # ---------------- RECALL ----------------

    elif mode == "recall":

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

    # ---------------- FORGET ----------------

    elif mode == "forget":

        prompt = f"""
You are an AI memory deletion extractor.

Your task is to identify which memory attribute the user wants to forget.

Return ONLY valid JSON.

Rules:

1. Return only JSON.
2. No explanation.
3. No markdown.

If no attribute is found return:

{{
    "attribute": ""
}}

Examples:

Input:
Forget my favorite language.

Output:
{{
    "attribute": "favorite_language"
}}

Input:
Delete my birthday.

Output:
{{
    "attribute": "birthday"
}}

Input:
Remove my favorite fruit.

Output:
{{
    "attribute": "favorite_fruit"
}}

Input:
Erase my name.

Output:
{{
    "attribute": "name"
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