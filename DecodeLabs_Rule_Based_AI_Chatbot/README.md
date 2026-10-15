# DecodeLabs — Rule-Based AI Chatbot (Project 1)

A beginner-friendly Python chatbot built for DecodeLabs Artificial Intelligence Project 1. It responds to predefined messages using `if-elif-else` conditions and runs in a continuous loop until the user exits.

## Features

- Handles greetings such as `hello`, `hi`, and `good morning`
- Responds to questions about its name and how it is doing
- Shows the current time and date
- Includes help, thanks, joke, and basic AI responses
- Uses a continuous `while` loop
- Exits on `bye`, `goodbye`, `exit`, `quit`, or `stop`
- Handles blank input and Ctrl+C / end-of-input gracefully
- Uses only Python's standard library (no extra packages required)

## Requirements

- Python 3.8 or newer

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python chatbot.py
   ```

   On some systems, use `python3 chatbot.py`.

## Example conversation

```text
DecodeBot: Hello! Type 'help' for commands or 'bye' to exit.
You: hello
DecodeBot: Hi there! What would you like to talk about?
You: what is your name
DecodeBot: My name is DecodeBot, a simple rule-based chatbot.
You: tell me a joke
DecodeBot: Why did the computer get cold? It left its Windows open!
You: bye
DecodeBot: DecodeBot says goodbye!
```

## Concepts used

- Variables and strings
- Functions
- `if`, `elif`, and `else`
- `while` loop
- User input and output
- String methods such as `strip()` and `lower()`
- Python standard library (`datetime`, `random`)

## Project structure

```text
DecodeLabs_Rule_Based_AI_Chatbot/
├── chatbot.py
├── test_chatbot.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Upload to GitHub

1. Create a new repository on GitHub, for example `DecodeLabs-Rule-Based-AI-Chatbot`.
2. Upload the files in this folder, or run these commands from this folder:

   ```bash
   git init
   git add .
   git commit -m "Complete DecodeLabs rule-based AI chatbot project"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/DecodeLabs-Rule-Based-AI-Chatbot.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` with your GitHub username. Do not include the angle brackets.

## Learning note

This is a rule-based chatbot, not a machine-learning model. Its responses come from explicitly programmed conditions, matching the core requirement of Project 1.
