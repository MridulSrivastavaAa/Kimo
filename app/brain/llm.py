from ollama import chat
from config.settings import MODEL_NAME
from app.conversation.manager import ConversationManager

conversation = ConversationManager()


def ask_llm(prompt: str) -> str:
    # User message add karo
    conversation.add_user_message(prompt)

    # Ollama ko poori conversation bhejo
    response = chat(
        model=MODEL_NAME,
        messages=conversation.get_messages(),
    )

    # Assistant ka response nikalo
    reply = response["message"]["content"]

    # Conversation me save karo
    conversation.add_assistant_message(reply)

    return reply
def stream_llm(prompt: str):
    conversation.add_user_message(prompt)

    stream = chat(
        model=MODEL_NAME,
        messages=conversation.get_messages(),
        stream=True,
    )

    full_response = ""

    for chunk in stream:
        text = chunk["message"]["content"]
        full_response += text
        yield text

    conversation.add_assistant_message(full_response)