import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()

def get_ai_response(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

st.title("🤖 AI Chat Personal Agent")
st.write("Your simple AI assistant - ask me anything!")

if prompt := st.chat_input("What can I help you with?"):
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(prompt)
            st.write(ai_response)
