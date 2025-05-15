import streamlit as st
from utils.chat import answer_question, process_image
from utils.quiz import run_quiz

st.set_page_config(page_title="CS-with AbdulBasit", layout="centered")

st.title("🤖 CS-with AbdulBasit")
st.write("Your AI tutor for O-level/IGCSE Computer Science")

mode = st.sidebar.selectbox("Choose Mode", ["Ask a Question", "Upload Question Image", "Quiz Mode"])

if mode == "Ask a Question":
    user_input = st.text_area("Enter your question:")
    if st.button("Get Answer"):
        if user_input.strip():
            response = answer_question(user_input)
            st.markdown(response)
        else:
            st.warning("Please enter a question.")

elif mode == "Upload Question Image":
    uploaded_file = st.file_uploader("Upload an image (question):", type=["png", "jpg", "jpeg"])
    if uploaded_file and st.button("Get Answer from Image"):
        response = process_image(uploaded_file)
        st.markdown(response)

elif mode == "Quiz Mode":
    run_quiz()