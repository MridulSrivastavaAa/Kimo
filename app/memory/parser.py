import json
import re


def parse_json(text: str):
    """
    Extract and parse JSON from LLM response.
    """

    # Remove markdown code fences
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Find first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in response.")

    json_text = match.group()

    return json.loads(json_text)