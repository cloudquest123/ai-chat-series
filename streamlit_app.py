import streamlit as st  # Create web interface
from openai import OpenAI  # Connect to ChatGPT
import os  # Read environment variables
from dotenv import load_dotenv  # Load API key from .env file

# Load environment variables - keeps API key secure
load_dotenv()

@st.cache_resource  # Cache client for better performance
def get_openai_client():
    """Initialize and cache the OpenAI client"""
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()

def get_ai_response(user_message):
    """Send user message to OpenAI and get intelligent response"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Which AI model to use
            messages=[{"role": "user", "content": user_message}],  # Format message
            max_tokens=300  # Limit response length
        )
        return response.choices[0].message.content  # Extract AI's reply
    except Exception as e:
        return f"Error: {e}"  # Handle errors gracefully

st.title("🤖 AI Chat Personal Agent")
st.write("Your simple AI assistant - ask me anything!")

# Chat interface
if prompt := st.chat_input("What can I help you with?"):  # User types message
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):  # Show loading animation
            ai_response = get_ai_response(prompt)  # Call OpenAI API
            st.write(ai_response)  # Display response
