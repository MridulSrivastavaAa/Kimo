from app.memory.manager import MemoryManager


class MemoryContext:

    def __init__(self):
        self.memory = MemoryManager()

    def get_all_memories(self):
        return self.memory.get_all_memories()

    def build_context(self, prompt: str):

        memories = self.get_all_memories()

        if not memories:
            return (
                "You are Kimo, an offline AI assistant.\n"
                "No user memories are available."
            )

        prompt = prompt.lower()

        context = "You are Kimo, an offline AI assistant.\n\n"
        context += "User Memories:\n"

        found = False
        added = set()   # Same attribute ko ek hi baar add karega

        for memory in memories:

            attribute = memory["attribute"].lower()
            value = memory["value"]

            if attribute in added:
                continue

            keywords = attribute.split("_")

            for keyword in keywords:
                if keyword in prompt:
                    context += (
                        f"- {attribute.replace('_', ' ').title()}: {value}\n"
                    )
                    added.add(attribute)
                    found = True
                    break

        if not found:
            context += "No relevant memory found.\n"

        return context