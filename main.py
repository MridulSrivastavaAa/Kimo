from app.brain.brain import Brain
from app.core.logger import logger


def main():
    logger.info("Kimo Started")

    brain = Brain()

    print("=" * 50)
    print("🤖 Kimo AI Assistant")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        # Log user input
        logger.info(f"User: {user_input}")

        # Exit condition
        if user_input.lower() == "exit":
            print("\nKimo: Goodbye!")
            logger.info("Kimo Stopped")
            break

        try:
            print("\nKimo: ", end="", flush=True)

            full_response = ""

            for chunk in brain.stream(user_input):
                print(chunk, end="", flush=True)
                full_response += chunk

            logger.info(f"Kimo: {full_response}")

            print()

        except Exception as e:
            logger.exception(f"Unexpected Error: {e}")
            print("\nKimo: Sorry, something went wrong.")


if __name__ == "__main__":
    main()