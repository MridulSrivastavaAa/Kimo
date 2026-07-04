def route(text: str) -> str:

    text = text.lower().strip()

    # -------- Recall Memory --------

    recall_patterns = [
        "what is my",
        "what's my",
        "who am i",
        "where do i live",
        "do you remember",
    ]

    for pattern in recall_patterns:
        if pattern in text:
            return "recall_memory"

    # -------- Save Memory --------

    save_patterns = [
        "remember",
        "my name is",
        "my birthday is",
        "i live in",
        "my favorite",
        "my favourite",
    ]

    for pattern in save_patterns:

        if text.startswith(pattern):
            return "save_memory"

    if text.startswith("i am "):
        return "save_memory"

    if text.startswith("i'm "):
        return "save_memory"

    # -------- Default --------

    return "chat"