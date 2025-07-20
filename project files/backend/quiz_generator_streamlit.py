import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("🧠 EduTutor AI - Quiz Generator")
st.write("Generate quizzes using OpenAI's GPT-3.5-turbo.")

# User input
topic = st.text_input("Enter a quiz topic:", "Photosynthesis")
num_questions = st.slider("Number of questions:", 1, 10, 5)

if st.button("Generate Quiz"):
    with st.spinner("Generating quiz..."):
        prompt = f"Generate {num_questions} multiple-choice questions on the topic: {topic}. Each question should have four options and mention the correct answer."

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            quiz = response.choices[0].message.content
            st.markdown("### Quiz:")
            st.markdown(quiz)
        except Exception as e:
            st.error(f"An error occurred: {e}")
