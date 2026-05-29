
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit page config
st.set_page_config(
    page_title="AI/ML Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 AI/ML Chatbot")

st.write("Ask questions related to AI, ML, Deep Learning, NLP, Python, etc.")

# User input
user_question = st.text_input("Enter your question")

# Allowed AI/ML keywords
allowed_topics = [
    "ai",
    "ml",
    "machine learning",
    "deep learning",
    "python",
    "nlp",
    "neural network",
    "computer vision",
    "data science"
]

# Ask button
if st.button("Ask AI"):

    if user_question:

        # Check topic
        if any(word in user_question.lower() for word in allowed_topics):

            with st.spinner("Thinking..."):

                response = client.chat.completions.create(
                    #changing aftet a time expire model
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": """
                            You are an AI/ML expert chatbot.
                            Only answer AI and Machine Learning related questions.
                            If question is unrelated, refuse politely.
                            """
                        },
                        {
                            "role": "user",
                            "content": user_question
                        }
                    ]
                )

                answer = response.choices[0].message.content

                st.success(answer)

        else:
            st.warning("⚠️ Please ask only AI/ML related questions.")
