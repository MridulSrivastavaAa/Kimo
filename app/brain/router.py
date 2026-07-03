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
        "i am ",
        "i'm ",
        "my birthday is",
        "i live in",
        "my favorite",
        "my favourite",
    ]

    for pattern in save_patterns:
        if pattern in text:
            return "save_memory"

    # -------- Default --------

    return "chat"