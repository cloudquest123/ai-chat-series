# Episode 7: Bare Minimum AI App

## Table of Contents
- [What You'll Build](#what-youll-build)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Features](#features)
- [How It Works](#how-it-works)
- [Code Structure](#code-structure)
- [Expected Output](#expected-output)
- [Troubleshooting](#troubleshooting)
- [Key Concepts Learned](#key-concepts-learned)
- [What Changed from Episode 6](#what-changed-from-episode-6)
- [Next Episode](#next-episode)
- [Series Progress](#series-progress)
- [Repository Navigation](#repository-navigation)

## What You'll Build
Your first real AI chat application! This combines the CLI foundation from Episode 5 with the OpenAI API connection from Episode 6 into a working AI chatbot.

## Prerequisites
- Completed Episode 5 (CLI Basics)
- Completed Episode 6 (OpenAI API Test)
- OpenAI API key configured in .env file
- Python 3.8+
- Virtual environment set up

## Setup Instructions

### 1. Get the Code
```bash
# Clone the repository (if you haven't already)
git clone https://github.com/cloudquest123/ai-chat-series.git
cd ai-chat-series

# Switch to this episode's branch
git checkout episode-07-complete-app

# Pull latest changes
git pull origin episode-07-complete-app
```

### 2. Activate Your Virtual Environment
```bash
# Mac/Linux
source ai_project/bin/activate

# Windows
ai_project\Scripts\activate
```

You should see `(ai_project)` in your prompt.

### 3. Verify Packages Installed
```bash
# These should already be installed from Episode 6
pip install openai python-dotenv
```

### 4. Verify Environment Variables
Make sure your `.env` file exists with your OpenAI API key:
```
OPENAI_API_KEY=your-openai-api-key-here
```

## Running the Application

```bash
python bare_minimum_ai.py
```

**To stop the program**: Type `quit`, `exit`, or `bye`

## Features
- ✅ **Real AI Conversations**: Uses OpenAI GPT-3.5-turbo
- ✅ **CLI Interface**: Terminal-based chat
- ✅ **Continuous Loop**: Chat until you quit
- ✅ **Error Handling**: Graceful error messages
- ✅ **Clean Exit**: Multiple exit commands

## How It Works
1. Load API key from .env file
2. Initialize OpenAI client
3. Display welcome message
4. Enter conversation loop:
   - Get user input
   - Send to OpenAI API
   - Display AI response
   - Repeat until user quits
5. Exit gracefully

## Code Structure

### Main Components
```python
# 1. Setup: Import libraries and initialize client
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. AI Function: Get response from OpenAI
def get_ai_response(user_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
        max_tokens=150
    )
    return response.choices[0].message.content

# 3. CLI Loop: Get input, call AI, display response
while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Goodbye!")
        break

    ai_response = get_ai_response(user_input)
    print(f"AI: {ai_response}")
```

## Expected Output
```
🤖 Bare Minimum AI Chat
Type 'quit' to exit

You: What is artificial intelligence?
AI: Artificial intelligence (AI) refers to computer systems that can perform tasks that typically require human intelligence...

You: How does Python work?
AI: Python is an interpreted programming language that executes code line by line...

You: quit
Goodbye!
```

## Troubleshooting

### API Errors
- Check your .env file has the correct API key
- Verify your OpenAI account has credits
- Check your internet connection

### Import Errors
```bash
# Reinstall packages
pip install --upgrade openai python-dotenv
```

### Rate Limits
If you get rate limit errors, wait a few seconds between requests.

## Key Concepts Learned
- **Merging Components**: Combining CLI loop + API calls
- **Function Design**: Creating reusable AI response function
- **Error Handling**: Try/except for API failures
- **User Experience**: Clean input/output flow
- **Incremental Building**: Step-by-step construction

## What Changed from Episode 6

### Episode 6 (openai_test.py)
- Single API test
- One-time execution
- Success verification only

### Episode 7 (bare_minimum_ai.py)
- Continuous conversation loop
- Multiple API calls
- Full chat experience
- User-controlled exit

**Key Difference**:
```python
# Episode 6: Single test
response = test_openai_connection()

# Episode 7: Continuous chat
while True:
    ai_response = get_ai_response(user_input)
    print(f"AI: {ai_response}")
```

## Next Episode
Episode 8 will transform this CLI app into a beautiful web interface using Streamlit - same AI logic, professional web design!

## Series Progress
- ✅ Episode 1: Introduction to the challenge
- ✅ Episode 2: What is AI?
- ✅ Episode 3: What tools you need
- ✅ Episode 4a: Mac installation
- ✅ Episode 4b: Windows installation
- ✅ Episode 5: CLI basics
- ✅ Episode 6: API connection testing
- 🎯 **Episode 7: First AI chat app** (You are here)
- ⏭️ Episode 8: Web interface with Streamlit
- ⏭️ Episode 9: Conversation memory
- ⏭️ Episode 10: Persistent storage

## Repository Navigation
- Switch to different episodes: `git checkout episode-XX-name`
- See all episodes: `git branch -a`
- Start from scratch: `git checkout main`

---

🎉 **Congratulations!** You've built your first working AI application from scratch!
