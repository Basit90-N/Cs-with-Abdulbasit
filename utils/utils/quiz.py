import streamlit as st

sample_questions = [
    {"q": "What is the purpose of a logic gate?", "a": "To perform a logical operation on one or more binary inputs."},
    {"q": "What does RAM stand for?", "a": "Random Access Memory"},
    {"q": "Give one example of secondary storage.", "a": "Hard drive or SSD."}
]

def run_quiz():
    score = 0
    st.subheader("🧠 Quiz Time!")
    for i, item in enumerate(sample_questions):
        answer = st.text_input(f"Q{i+1}: {item['q']}")
        if answer:
            if answer.strip().lower() in item["a"].lower():
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. Correct answer: {item['a']}")
    st.info(f"Final Score: {score}/{len(sample_questions)}")
