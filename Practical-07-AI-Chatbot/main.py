import re
import random

rules = [
    (r"\b(hello|hii|good morning|good evening)\b", [
        "Hello! How can i help you?",
        "Hii! Nice to meet you.",
        "Hey! What can I do for you?"
    ]),
    (r"\b(what is your name|your name|who are you)\b", [
        "My name is SimpleBot.",
        "I am SimpleBot, a rule-based AI Chatbot."
    ]),
    (r"\b(how are you| how r u)\b", [
        "I am fine, thanks for asking.",
        "Iam doing great!",
        "I am ready to help you."
    ]),
    (r"\b(college|university)\b", [
        "College is an important part of learning and development.",
        "I can help you with your college-related questions."
    ]),
    (r"\b(programming|coding|python|java|c|c\+\+)\b", [
        "Programming is the process of solving problems using code.",
        "Python, Java and C++ are popular higher level programming languages"
    ]),
    (r"\b(artificial intelligence|ai|what is ai)\b", [
        "AI stands for Artificial Intelligence.",
        "Artificial Intelligence allows computers to perform tasks that normally require human intelligence."
    ]),
    (r"\b(machine learning|ml)\b", [
        "Machine Learning is a branch of AI where computers learn pattern from data."
    ]),
    (r"\b(thanks|thank you|thank)\b", [
        "You are most welcome.",
        "Happy to help you.",
        "No Problem."
    ]),
    (r"\b(bye|goodbye|see you)\b", [
        "Good Bye!",
        "See you later!",
        "Have a nice day!"
    ])
]

def chatbot(user_input):
    user_input = user_input.lower()
    for pattern, responses in rules:
        if re.search(pattern, user_input):
            return random.choice(responses)
    return "Sorry, I don't understand that. Please try asking something else."

print("=" * 45)
print(" SIMPLE AI CHATBOT")
print("=" * 45)
print("Type 'BYE' to exit the chatbot")
while True:
    user_input = input("\nYou: ")
    response = chatbot(user_input)
    print("Bot:", response)
    if re.search(r"\b(bye|goodbye|see you)\b", user_input.lower()):
        break