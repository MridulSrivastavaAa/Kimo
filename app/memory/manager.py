from app.storage.memory_repository import MemoryRepository
from app.memory.extractor import extract_memory


class MemoryManager:

    def __init__(self):
        self.repository = MemoryRepository()

    def save_memory(self, memory_type: str, attribute: str, value: str):
        self.repository.save_memory(
            memory_type,
            attribute,
            value,
        )

    def get_memory(self, attribute: str):
        return self.repository.get_memory(attribute)

    def get_all_memories(self):
        return self.repository.get_all_memories()

    def delete_memory(self, attribute: str):
        self.repository.delete_memory(attribute)

    def process_memory(self, text: str):
        try:
            memory = extract_memory(text, mode="save")

            if not memory:
                return False

            memory_type = memory.get("memory_type", "").strip()
            attribute = memory.get("attribute", "").strip()
            value = memory.get("value", "").strip()

            if not memory_type or not attribute or not value:
                return False

            self.save_memory(
                memory_type=memory_type,
                attribute=attribute,
                value=value,
            )

            return True

        except Exception as e:
            print(f"Memory Error: {e}")
            return False

    def recall_memory(self, text: str):
        try:
            memory = extract_memory(
                text,
                mode="recall",
            )

            if not memory:
                return "I don't remember."

            attribute = memory.get("attribute", "").strip()

            if not attribute:
                return "I don't remember."

            memory_data = self.get_memory(attribute)

            if not memory_data:
                return "I don't remember."

            value = memory_data["value"]

            return f"Your {attribute.replace('_', ' ')} is {value}."

        except Exception as e:
            print(f"Recall Error: {e}")
            return "I couldn't recall that memory."