
from ollama import chat

from config.settings import MODEL_NAME
from app.conversation.manager import ConversationManager
from app.memory.context import MemoryContext


conversation = ConversationManager()
memory_context = MemoryContext()


def ask_llm(prompt: str) -> str:

    # Memory context build karo
    context = memory_context.build_context(prompt)

    # Final prompt banao
    final_prompt = f"""
{context}

Current User Message:
{prompt}
"""

    # Conversation me final prompt save karo
    conversation.add_user_message(final_prompt)

    # Ollama ko conversation bhejo
    response = chat(
        model=MODEL_NAME,
        messages=conversation.get_messages(),
    )

    reply = response["message"]["content"]

    conversation.add_assistant_message(reply)

    return reply


def stream_llm(prompt: str):

    # Memory context build karo
    context = memory_context.build_context(prompt)

    # Final prompt banao
    final_prompt = f"""
{context}

Current User Message:
{prompt}
"""

    conversation.add_user_message(final_prompt)

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