"""
DecodeLabs - Artificial Intelligence Project 1
Rule-Based AI Chatbot

Run: python chatbot.py
This project uses Python if/elif/else logic and a continuous loop.
"""

import random
from datetime import datetime

BOT_NAME = "DecodeBot"

RESPONSES = {
    "greeting": [
        "Hello! Welcome to DecodeBot. How can I help you?",
        "Hi there! What would you like to talk about?",
        "Hey! Great to see you. Ask me something."
    ],
    "how_are_you": [
        "I'm doing great, thanks for asking!",
        "I'm just code, but I'm running smoothly. How are you?"
    ],
    "name": f"My name is {BOT_NAME}, a simple rule-based chatbot.",
    "help": (
        "You can say hello, ask how I am, ask my name, ask for the time/date, "
        "or type 'help' to see these options. Type 'bye' to exit."
    ),
    "thanks": "You're welcome! Happy to help.",
    "default": (
        "I'm not sure how to answer that yet. Try 'help' to see what I understand."
    ),
}


def get_response(user_message: str) -> str:
    """Return a response using simple, explicit rules."""
    message = user_message.strip().lower()

    if not message:
        return "Please type a message so I can respond."

    # Exit is handled in the main loop; this keeps get_response easy to test.
    if message in {"hi", "hello", "hey", "hii", "good morning", "good afternoon", "good evening"}:
        return random.choice(RESPONSES["greeting"])
    elif message in {"how are you", "how are you?", "how r you", "how r u"}:
        return random.choice(RESPONSES["how_are_you"])
    elif "your name" in message or message == "name":
        return RESPONSES["name"]
    elif message in {"help", "what can you do", "commands"}:
        return RESPONSES["help"]
    elif "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M %p") + "."
    elif "date" in message or "today" in message:
        return "Today's date is " + datetime.now().strftime("%d %B %Y") + "."
    elif "thank" in message or message == "thanks":
        return RESPONSES["thanks"]
    elif "joke" in message:
        return "Why did the computer get cold? It left its Windows open!"
    elif "ai" in message or "artificial intelligence" in message:
        return "AI stands for Artificial Intelligence. This chatbot uses rules, not machine learning."
    elif message in {"bye", "goodbye", "exit", "quit", "stop"}:
        return "Goodbye! Thanks for chatting with DecodeBot."
    else:
        return RESPONSES["default"]


def main() -> None:
    """Run the chatbot until the user enters an exit command."""
    print("=" * 48)
    print("        DecodeLabs | Rule-Based AI Chatbot")
    print("=" * 48)
    print(f"{BOT_NAME}: Hello! Type 'help' for commands or 'bye' to exit.")

    while True:
        try:
            user_message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Goodbye! Thanks for chatting.")
            break

        if user_message.lower() in {"bye", "goodbye", "exit", "quit", "stop"}:
            print(f"{BOT_NAME}: {RESPONSES['name'].split(',')[0]} says goodbye!")
            break

        print(f"{BOT_NAME}: {get_response(user_message)}")


if __name__ == "__main__":
    main()
