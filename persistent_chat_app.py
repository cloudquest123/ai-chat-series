#!/usr/bin/env python3
"""
Episode 10: Stateful Sessions with File Persistence
Saves conversations to files for persistence across browser sessions
"""

import streamlit as st  # Create web interface
from openai import OpenAI  # Connect to ChatGPT
import os  # Read environment variables
import json  # Save and load conversation data as JSON files
from datetime import datetime  # Create timestamp-based filenames
from pathlib import Path  # Handle file paths cross-platform
from dotenv import load_dotenv  # Load API key from .env file

# Load environment variables - keeps API key secure and separate from code
load_dotenv()

# Initialize OpenAI client with caching for better performance
@st.cache_resource  # Cache client so we don't recreate it on every rerun
def get_openai_client():
    """Create and cache the OpenAI client connection"""
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()  # Get the cached AI client

# Create conversations directory - this is where we store all conversation files
CONVERSATIONS_DIR = Path("conversations")  # Create a Path object for the folder
CONVERSATIONS_DIR.mkdir(exist_ok=True)  # Create folder if it doesn't exist

def save_conversation(messages, filename=None):
    """Save conversation to a JSON file for persistence across sessions"""
    if not filename:
        # Create a unique filename with timestamp if none provided
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: 20231201_143022
        filename = f"chat_{timestamp}.json"  # Example: chat_20231201_143022.json

    filepath = CONVERSATIONS_DIR / filename  # Full path to save the file
    with open(filepath, "w") as f:
        json.dump(messages, f, indent=2)  # Save messages as formatted JSON

    return filename  # Return filename so we can track which file we're using

def load_conversation(filename):
    """Load conversation from a JSON file to restore previous chat"""
    filepath = CONVERSATIONS_DIR / filename  # Full path to the saved file
    try:
        with open(filepath, "r") as f:
            return json.load(f)  # Load and return the conversation messages
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file not found or corrupted

def get_conversation_files():
    """Get list of all saved conversation files, sorted by newest first"""
    if not CONVERSATIONS_DIR.exists():
        return []  # No files if folder doesn't exist

    files = list(CONVERSATIONS_DIR.glob("*.json"))  # Find all JSON files
    # Sort by modification time - newest conversations appear first
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    return [f.name for f in files]  # Return just the filenames, not full paths

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

def format_conversation_preview(messages, max_length=50):
    """Create a short preview of conversation to display in sidebar"""
    if not messages:
        return "Empty conversation"  # No messages to preview

    # Find the first user message to use as preview
    first_user_message = next((msg["content"] for msg in messages if msg["role"] == "user"), "")
    if len(first_user_message) > max_length:
        return first_user_message[:max_length] + "..."  # Truncate long messages
    return first_user_message or "No preview available"

def main():
    """Main Streamlit application with file persistence"""
    st.title("💾 AI Chat with Persistent Memory")
    st.write("Your AI assistant that saves and remembers conversations across sessions!")

    # Sidebar for conversation management - the control center for file operations
    with st.sidebar:
        st.subheader("💬 Conversation Management")

        # Load existing conversation - show list of all saved conversations
        conversation_files = get_conversation_files()  # Get all saved JSON files
        if conversation_files:
            st.write("**Load Previous Conversation:**")
            for filename in conversation_files[:10]:  # Show last 10 conversations only
                messages = load_conversation(filename)  # Read the conversation from file
                preview = format_conversation_preview(messages)  # Create preview text
                timestamp = filename.replace("chat_", "").replace(".json", "")  # Clean filename

                # Button to load this conversation
                if st.button(f"📄 {timestamp}", key=f"load_{filename}"):
                    st.session_state.messages = messages  # Load messages into memory
                    st.session_state.current_filename = filename  # Track which file we're using
                    st.rerun()  # Refresh to display loaded conversation

                # Show preview of conversation
                st.caption(f"Preview: {preview}")
                st.divider()

        # Current conversation info - show what's currently active
        st.subheader("📊 Current Session")
        current_filename = getattr(st.session_state, 'current_filename', 'New conversation')
        st.write(f"**File:** {current_filename}")  # Which file we're working with

        messages_count = len(getattr(st.session_state, 'messages', []))
        st.write(f"**Messages:** {messages_count}")  # How many messages in conversation

        # Action buttons - Save and New Chat
        col1, col2 = st.columns(2)
        with col1:
            # Manual save button (though we auto-save after each message)
            if st.button("💾 Save"):
                if hasattr(st.session_state, 'messages') and st.session_state.messages:
                    filename = save_conversation(st.session_state.messages)  # Save to file
                    st.session_state.current_filename = filename  # Track filename
                    st.success(f"Saved as {filename}")
                else:
                    st.warning("No conversation to save")

        with col2:
            # Start a fresh conversation
            if st.button("🗑️ New Chat"):
                st.session_state.messages = []  # Clear all messages
                st.session_state.current_filename = "New conversation"  # Reset filename
                st.rerun()  # Refresh to show empty state

    # Initialize session state for conversation history and current file
    if "messages" not in st.session_state:
        st.session_state.messages = []  # Create empty list for messages

    if "current_filename" not in st.session_state:
        st.session_state.current_filename = "New conversation"  # Track active file

    # Display all previous messages from conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):  # Show as user or assistant
            st.write(message["content"])  # Display the message text

    # Chat input - when user types and presses Enter
    if prompt := st.chat_input("What can I help you with?"):
        # Step 1: Add user's message to conversation memory
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Step 2: Display user's message immediately
        with st.chat_message("user"):
            st.write(prompt)

        # Step 3: Get AI response using full conversation history
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):  # Show loading animation
                ai_response = get_ai_response(st.session_state.messages)  # Get AI reply
                st.write(ai_response)  # Display AI's response

                # Step 4: Add AI's response to conversation memory
                st.session_state.messages.append({"role": "assistant", "content": ai_response})

        # Step 5: AUTO-SAVE after each exchange - the magic of persistence!
        if st.session_state.messages:
            if st.session_state.current_filename == "New conversation":
                # First save - create new file with timestamp
                filename = save_conversation(st.session_state.messages)
                st.session_state.current_filename = filename  # Remember the filename
            else:
                # Update existing file - overwrite with latest conversation
                save_conversation(st.session_state.messages, st.session_state.current_filename)

if __name__ == "__main__":
    main()
