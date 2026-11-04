# Simple Rule-Based Chatbot

import re

print("Chatbot: Hello! Welcome to the chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()
    words = re.findall(r"\w+", user)  # whole words, so "which" does not match "hi"

    if "hello" in words or "hi" in words:
        print("Chatbot: Hello! How can I help you?")

    elif "your name" in user:
        print("Chatbot: I am a simple Python chatbot.")

    elif "how are you" in user:
        print("Chatbot: I am fine. Thank you!")

    elif "help" in user:
        print("Chatbot: Sure! Tell me what you need help with.")

    elif "thank" in user:
        print("Chatbot: You're welcome!")

    elif "bye" in user:
        print("Chatbot: Goodbye! Have a nice day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
