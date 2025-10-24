#!/usr/bin/env python3
"""
Episode 10: Stateful Sessions with File Persistence
Saves conversations to files for persistence across browser sessions
"""

import streamlit as st
from openai import OpenAI
import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()

# Create conversations directory if it doesn't exist
CONVERSATIONS_DIR = Path("conversations")
CONVERSATIONS_DIR.mkdir(exist_ok=True)

def save_conversation(messages, filename=None):
    """Save conversation to a JSON file"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_{timestamp}.json"

    filepath = CONVERSATIONS_DIR / filename
    with open(filepath, "w") as f:
        json.dump(messages, f, indent=2)

    return filename

def load_conversation(filename):
    """Load conversation from a JSON file"""
    filepath = CONVERSATIONS_DIR / filename
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_conversation_files():
    """Get list of saved conversation files"""
    if not CONVERSATIONS_DIR.exists():
        return []

    files = list(CONVERSATIONS_DIR.glob("*.json"))
    # Sort by modification time (newest first)
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    return [f.name for f in files]

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

def format_conversation_preview(messages, max_length=50):
    """Create a preview of the conversation for the sidebar"""
    if not messages:
        return "Empty conversation"

    first_user_message = next((msg["content"] for msg in messages if msg["role"] == "user"), "")
    if len(first_user_message) > max_length:
        return first_user_message[:max_length] + "..."
    return first_user_message or "No preview available"

def main():
    """Main Streamlit application with file persistence"""
    st.title("💾 AI Chat with Persistent Memory")
    st.write("Your AI assistant that saves and remembers conversations across sessions!")

    # Sidebar for conversation management
    with st.sidebar:
        st.subheader("💬 Conversation Management")

        # Load existing conversation
        conversation_files = get_conversation_files()
        if conversation_files:
            st.write("**Load Previous Conversation:**")
            for filename in conversation_files[:10]:  # Show last 10 conversations
                messages = load_conversation(filename)
                preview = format_conversation_preview(messages)
                timestamp = filename.replace("chat_", "").replace(".json", "")

                if st.button(f"📄 {timestamp}", key=f"load_{filename}"):
                    st.session_state.messages = messages
                    st.session_state.current_filename = filename
                    st.rerun()

                # Show preview
                st.caption(f"Preview: {preview}")
                st.divider()

        # Current conversation info
        st.subheader("📊 Current Session")
        current_filename = getattr(st.session_state, 'current_filename', 'New conversation')
        st.write(f"**File:** {current_filename}")

        messages_count = len(getattr(st.session_state, 'messages', []))
        st.write(f"**Messages:** {messages_count}")

        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save"):
                if hasattr(st.session_state, 'messages') and st.session_state.messages:
                    filename = save_conversation(st.session_state.messages)
                    st.session_state.current_filename = filename
                    st.success(f"Saved as {filename}")
                else:
                    st.warning("No conversation to save")

        with col2:
            if st.button("🗑️ New Chat"):
                st.session_state.messages = []
                st.session_state.current_filename = "New conversation"
                st.rerun()

    # Initialize session state for conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "current_filename" not in st.session_state:
        st.session_state.current_filename = "New conversation"

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

        # Auto-save after each exchange
        if st.session_state.messages:
            if st.session_state.current_filename == "New conversation":
                filename = save_conversation(st.session_state.messages)
                st.session_state.current_filename = filename
            else:
                save_conversation(st.session_state.messages, st.session_state.current_filename)

if __name__ == "__main__":
    main()
