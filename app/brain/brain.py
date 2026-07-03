from app.brain.llm import ask_llm, stream_llm


class Brain:

    def think(self, prompt: str) -> str:
        """
        Return complete response.
        """
        return ask_llm(prompt)

    def stream(self, prompt: str):
        """
        Stream response chunk by chunk.
        """
        yield from stream_llm(prompt)