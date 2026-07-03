from app.storage.database import Database


class MemoryRepository:

    def __init__(self):
        self.db = Database()
        self.db.initialize()

    def save_memory(self, memory_type: str, attribute: str, value: str):
        query = """
        INSERT INTO memories (memory_type, attribute, value)
        VALUES (?, ?, ?)
        """
        self.db.execute(query, (memory_type, attribute, value))

    def get_memory(self, attribute: str):
        query = """
        SELECT memory_type, attribute, value
        FROM memories
        WHERE attribute = ?
        ORDER BY id DESC
        LIMIT 1
        """

        result = self.db.fetchone(query, (attribute,))

        if result:
            return {
                "memory_type": result[0],
                "attribute": result[1],
                "value": result[2]
            }

        return None

    def get_all_memories(self):
        query = """
        SELECT memory_type, attribute, value
        FROM memories
        """

        results = self.db.fetchall(query)

        memories = []

        for row in results:
            memories.append({
                "memory_type": row[0],
                "attribute": row[1],
                "value": row[2]
            })

        return memories

    def delete_memory(self, attribute: str):
        query = """
        DELETE FROM memories
        WHERE attribute = ?
        """

        self.db.execute(query, (attribute,))