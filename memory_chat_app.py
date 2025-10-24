#!/usr/bin/env python3
"""
Episode 9: Remembering Conversations with OpenAI
Adds conversation memory within a single session using Streamlit session state
"""

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()

def get_ai_response(messages):
    """Send conversation history to OpenAI and get the response"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

def main():
    """Main Streamlit application with conversation memory"""
    st.title("🧠 AI Chat with Memory")
    st.write("Your AI assistant that remembers our conversation!")

    # Initialize session state for conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What can I help you with?"):
        # Add user message to conversation history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Get AI response using full conversation history
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                ai_response = get_ai_response(st.session_state.messages)
                st.write(ai_response)

                # Add AI response to conversation history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Sidebar with conversation info
    with st.sidebar:
        st.subheader("💬 Conversation Info")
        st.write(f"Messages in conversation: {len(st.session_state.messages)}")

        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()
