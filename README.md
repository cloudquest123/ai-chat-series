# Episode 6: Connecting to OpenAI (API Test)

## Table of Contents
- [What You'll Build](#what-youll-build)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Features](#features)
- [Environment Variables](#environment-variables)
- [Expected Output](#expected-output)
- [Troubleshooting](#troubleshooting)
- [Key Concepts Learned](#key-concepts-learned)
- [API Structure](#api-structure)
- [Security Note](#security-note)
- [Next Episode](#next-episode)
- [Series Progress](#series-progress)
- [Repository Navigation](#repository-navigation)

## What You'll Build
A simple test script to verify your OpenAI API connection works before building the full chat application.

## Prerequisites
- Completed Episode 5 (CLI Basics)
- OpenAI API key from [platform.openai.com](https://platform.openai.com)
- Python 3.8+
- Virtual environment set up

## Setup Instructions

### 1. Get the Code 
```bash
# Clone the repository
git clone https://github.com/cloudquest123/ai-chat-series.git
cd ai-chat-series

# Switch to this episode's branch  
git checkout episode-06-openai-connect

# Pull latest changes
git pull origin episode-06-openai-connect
```

### 2. Activate Your Virtual Environment
**Note**: You already created `ai_project` in Episodes 4a/4b - just activate it:

```bash
# Mac/Linux
source ai_project/bin/activate

# Windows
ai_project\Scripts\activate
```

**Only if you skipped Episodes 4a/4b** - create the virtual environment first:
```bash
# Mac/Linux - Create virtual environment
python3 -m venv ai_project

# Windows - Create virtual environment  
python -m venv ai_project
```

You should see `(ai_project)` in your prompt.

### 3. Install Required Packages
```bash
pip install openai python-dotenv
```

### 4. Set Up Environment Variables
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Running the Application

```bash
python openai_test.py
```

**To stop the program**: Press `Ctrl+C` (Mac/Windows/Linux)

## Features
- Secure API key storage using .env files
- Simple OpenAI API connection test
- Error handling for connection issues
- Success/failure feedback
- **No chat functionality yet** - pure API testing

## How It Works
1. Load API key from .env file
2. Initialize OpenAI client
3. Send test message to API
4. Display response or error
5. Foundation for Episode 7's chat app

## Environment Variables
Create a `.env` file with:
```
OPENAI_API_KEY=your-openai-api-key-here
```

## Expected Output
```
OpenAI API Connection Test
------------------------------
API Test Result:
AI Response: Connection successful!

✅ OpenAI API connection successful!
```

## Troubleshooting
If the connection fails, check:
1. Your API key in the .env file
2. Your internet connection
3. Your OpenAI account has credits
4. The API key has the correct permissions

## Key Concepts Learned
- Environment variable management with python-dotenv
- OpenAI Python library usage
- API authentication
- Error handling with try/except blocks
- Basic API request structure

## API Structure
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
```

## Next Episode
Episode 7 will combine this API connection with the CLI foundation from Episode 5 to create our first working AI chat application.

## Security Note
Never commit your .env file to version control. The .env.example file shows the format without exposing your actual API key.

## Series Progress
- ✅ Episode 1: Introduction to the challenge
- ✅ Episode 2: What is technology?
- ✅ Episode 3: What tools you need
- ✅ Episode 4a: Mac installation
- ✅ Episode 4b: Windows installation
- ✅ Episode 5: CLI basics
- 🎯 **Episode 6: API connection testing** (You are here)
- ⏭️ Episode 7: First working chat app
- ⏭️ Episodes 8-10: Advanced features

## Repository Navigation
- Switch to different episodes: `git checkout episode-XX-name`
- See all episodes: `git branch -a`
- Start from scratch: `git checkout main`