import random

def answer_question(prompt):
    question = prompt.lower()

    if "binary" in question:
        return "📘 Binary is a base-2 number system that uses only 0 and 1. It is the fundamental language of computers."

    elif "logic gate" in question:
        return "🔌 Logic gates are digital circuits that perform Boolean algebra. Common gates include AND, OR, and NOT."

    elif "pseudocode" in question:
        return "📝 Pseudocode is a way to design algorithms using plain English before actual coding."

    else:
        return "❓ Sorry, I don’t know the answer to that yet. Try asking about binary, logic gates, or pseudocode."


def process_image(image_file):
    return "📷 Extracted text from image and processed the question (simulated)."
