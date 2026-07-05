from app.brain.llm import ask_llm, stream_llm
from app.brain.router import route
from app.memory.manager import MemoryManager


class Brain:

    def __init__(self):
        self.memory = MemoryManager()

    def think(self, prompt: str):

        intent = route(prompt)
        print(f"Intent -> {intent}")

        # -------- Save Memory --------

        if intent == "save_memory":
            success = self.memory.process_memory(prompt)

            if success:
                return "Okay! I'll remember that."

            return "Sorry, I couldn't save that."

        # -------- Recall Memory --------

        elif intent == "recall_memory":
            return self.memory.recall_memory(prompt)

        # -------- Forget Memory --------

        elif intent == "forget_memory":
            return self.memory.forget_memory(prompt)

        # -------- Chat --------

        return ask_llm(prompt)

    def stream(self, prompt: str):

        intent = route(prompt)
        print(f"Intent -> {intent}")

        # -------- Save Memory --------

        if intent == "save_memory":
            success = self.memory.process_memory(prompt)

            if success:
                yield "Okay! I'll remember that."
            else:
                yield "Sorry, I couldn't save that."

            return

        # -------- Recall Memory --------

        elif intent == "recall_memory":
            yield self.memory.recall_memory(prompt)
            return

        # -------- Forget Memory --------

        elif intent == "forget_memory":
            yield self.memory.forget_memory(prompt)
            return

        # -------- Chat --------

        yield from stream_llm(prompt)