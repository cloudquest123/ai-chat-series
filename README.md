# Episode 5: Bare Minimum CLI Application (No AI)

## Table of Contents
- [What You'll Build](#what-youll-build)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Features](#features)
- [How It Works](#how-it-works)
- [Key Concepts Learned](#key-concepts-learned)
- [Code Structure](#code-structure)
- [Next Episode](#next-episode)
- [Series Progress](#series-progress)
- [Repository Navigation](#repository-navigation)

## What You'll Build
A simple command-line interface that accepts user input and echoes it back. This is the foundation for our chat application.

## Prerequisites
- Completed Episodes 1-4 (Python and VS Code installation)
- Python 3.8+
- Virtual environment set up

## Setup Instructions

### 1. Get the Code 
```bash
# Clone the repository
git clone https://github.com/cloudquest123/ai-chat-series.git
cd ai-chat-series

# Switch to this episode's branch  
git checkout episode-05-cli-app

# Pull latest changes
git pull origin episode-05-cli-app
```

### 2. Create and Activate Virtual Environment
```bash
# Mac/Linux - Create virtual environment
python3 -m venv ai_project

# Windows - Create virtual environment  
python -m venv ai_project
```

### 3. Activate Virtual Environment
```bash
# Mac/Linux
source ai_project/bin/activate

# Windows
ai_project\Scripts\activate
```

You should see `(ai_project)` in your prompt.

## Running the Application

```bash
python cli_basics.py
```

**Expected Output:**
```
Simple CLI App
Type 'quit' to exit
------------------------------

You: hello world
Echo: hello world

You: this is working
Echo: this is working

You: quit
Goodbye!
```

## Features
- Simple input/output loop
- Multiple exit commands (quit, exit, bye)
- Input validation (skips empty inputs)
- Clean exit handling
- **No AI involved** - pure CLI mechanics

## How It Works
1. User types a message
2. Program echoes the message back
3. Continues until user types 'quit'
4. Foundation for adding AI in later episodes

## Key Concepts Learned
- Python while loops
- User input handling with `input()`
- String manipulation with `.strip()` and `.lower()`
- Conditional logic for exit conditions
- Function organization with `main()`

## Code Structure
```python
def main():
    # Print welcome message
    # Start infinite loop
    # Get user input
    # Check for exit conditions
    # Echo the input back
    # Repeat until quit
```

**Key Points:**
- **No AI yet** - this is just the CLI foundation
- **Echo functionality** - proves input/output works
- **Clean structure** - ready for AI integration

## Next Episode
Episode 6 will test connecting to the OpenAI API before we combine CLI with AI in Episode 7.

## Series Progress
- ✅ Episode 1: Introduction to the challenge
- ✅ Episode 2: What is technology?
- ✅ Episode 3: What tools you need
- ✅ Episode 4a: Mac installation
- ✅ Episode 4b: Windows installation
- 🎯 **Episode 5: CLI basics** (You are here)
- ⏭️ Episode 6: API connection testing
- ⏭️ Episode 7: First working chat app
- ⏭️ Episodes 8-10: Advanced features

## Repository Navigation
- Switch to different episodes: `git checkout episode-XX-name`
- See all episodes: `git branch -a`
- Start from scratch: `git checkout main`
