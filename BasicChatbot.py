def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    # Convert to lowercase and remove extra spaces/punctuation so matching is easy
    message = user_input.lower().strip().strip("!?.")

    if message in ("hello", "hi", "hey"):
        return "Hi, how can i help you?"
    elif message in ("how are you", "how are you doing"):
        return "I'm fine, thanks!"
    elif message in ("what is your name", "who are you", "your name"):
        return "I'm a simple chatbot built with Python."
    elif message in ("what can you do", "help"):
        return "I can reply to: hello, how are you, what is your name, and bye."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def chatbot():
    """Run the chat loop until the user says bye."""
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        # Ignore empty input
        if user_input.strip() == "":
            print("Chatbot: Please type something.")
            continue

        response = get_response(user_input)
        print("Chatbot:", response)

        # Stop the loop when the user says goodbye
        if response == "Goodbye!":
            break


if __name__ == "__main__":
    chatbot()