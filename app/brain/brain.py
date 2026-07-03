from app.brain.llm import ask_llm, stream_llm
from app.brain.router import route
from app.memory.manager import MemoryManager


class Brain:

    def __init__(self):
        self.memory = MemoryManager()

    def think(self, prompt: str):

        intent = route(prompt)
        print(f"Intent -> {intent}")

        if intent == "save_memory":
            success = self.memory.process_memory(prompt)

            if success:
                return "Okay! I'll remember that."

            return "Sorry, I couldn't save that."

        elif intent == "recall_memory":
            return self.memory.recall_memory(prompt)

        return ask_llm(prompt)

    def stream(self, prompt: str):

        intent = route(prompt)
        print(f"Intent -> {intent}")

        if intent == "save_memory":
            success = self.memory.process_memory(prompt)

            if success:
                yield "Okay! I'll remember that."
            else:
                yield "Sorry, I couldn't save that."

            return

        elif intent == "recall_memory":
            yield self.memory.recall_memory(prompt)
            return

        yield from stream_llm(prompt)