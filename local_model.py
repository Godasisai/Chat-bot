def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! I'm your local AI chatbot."
    elif "your name" in user_input:
        return "I'm called LocalBot, your offline assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that yet. I'm still learning offline!"