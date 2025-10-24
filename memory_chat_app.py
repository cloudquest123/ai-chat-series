#!/usr/bin/env python3
"""
Episode 9: Remembering Conversations with OpenAI
Adds conversation memory within a single session using Streamlit session state
"""

import streamlit as st  # Create web interface
from openai import OpenAI  # Connect to ChatGPT
import os  # Read environment variables
from dotenv import load_dotenv  # Load API key from .env file

# Load environment variables - keeps API key secure and separate from code
load_dotenv()

# Initialize OpenAI client with caching for better performance
@st.cache_resource  # Cache client so we don't recreate it on every rerun
def get_openai_client():
    """Create and cache the OpenAI client connection"""
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()  # Get the cached AI client

def get_ai_response(messages):
    """Send full conversation history to OpenAI and get intelligent response"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Which AI model to use
            messages=messages,  # Send ENTIRE conversation history for context
            max_tokens=300  # Limit response length
        )
        return response.choices[0].message.content  # Extract AI's reply

    except Exception as e:
        return f"Error: {e}"  # Handle errors gracefully

def main():
    """Main Streamlit application with conversation memory"""
    st.title("🧠 AI Chat with Memory")
    st.write("Your AI assistant that remembers our conversation!")

    # Initialize session state for conversation history - this is the KEY to memory!
    # Session state persists data between reruns of the app
    if "messages" not in st.session_state:
        st.session_state.messages = []  # Create empty list to store all messages

    # Display all previous messages from conversation history
    # This shows the entire conversation every time the page reruns
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):  # Show as user or assistant
            st.write(message["content"])  # Display the message text

    # Chat input - when user types and presses Enter
    if prompt := st.chat_input("What can I help you with?"):
        # Step 1: Add user's message to our conversation memory
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Step 2: Display user's message immediately
        with st.chat_message("user"):
            st.write(prompt)

        # Step 3: Get AI response using FULL conversation history (this is the magic!)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):  # Show loading animation
                # Pass entire conversation history so AI knows context
                ai_response = get_ai_response(st.session_state.messages)
                st.write(ai_response)  # Display AI's response

                # Step 4: Add AI's response to conversation memory too
                st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Sidebar with conversation info and controls
    with st.sidebar:
        st.subheader("💬 Conversation Info")
        st.write(f"Messages in conversation: {len(st.session_state.messages)}")  # Show count

        # Button to clear all conversation history and start fresh
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []  # Reset to empty list
            st.rerun()  # Refresh the app to show empty state

if __name__ == "__main__":
    main()
