# Episode 4b: Installing Tools - Windows Version

## Table of Contents
- [What You'll Learn](#what-youll-learn)
- [Installation Steps](#installation-steps)
- [Verification Commands](#verification-commands)
- [Troubleshooting](#troubleshooting)
- [Next Episode](#next-episode)
- [Series Progress](#series-progress)
- [Repository Navigation](#repository-navigation)

## What You'll Learn
Complete Windows installation walkthrough for Python, VS Code, and setting up your development environment.

## Installation Steps

### 1. Python Installation (Windows)
1. Go to [python.org](https://python.org)
2. Download the `.exe` installer
3. **CRITICAL**: Check "Add Python to PATH" checkbox
4. Click "Install Now"

⚠️ **Important**: The "Add Python to PATH" checkbox is crucial - don't skip it!

### 2. Verify Python Installation
Open Command Prompt or PowerShell and run:

```cmd
# Check Python version (Windows uses 'python', not 'python3')
python --version

# Check pip version
pip --version
```

You should see version numbers for both commands.

### 3. VS Code Installation (Windows)
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download the `.exe` installer
3. Run installer with default settings
4. VS Code will be added to Start menu and desktop

### 4. Virtual Environment Setup
Create an isolated Python environment for your project:

```cmd
# Create project folder
mkdir ai-chat-project
cd ai-chat-project

# Create virtual environment
python -m venv ai-env

# Activate environment (Windows)
ai-env\Scripts\activate

# You should see (ai-env) in your prompt
```

### 5. Install Required Libraries
With your virtual environment active:

```cmd
# Install the libraries we need
pip install openai python-dotenv

# Verify installation
pip list
```

## Verification Commands
Run these to confirm everything works:

```cmd
# Python and pip working
python --version
pip --version

# Virtual environment active (PowerShell)
echo $env:VIRTUAL_ENV

# Virtual environment active (Command Prompt)
echo %VIRTUAL_ENV%

# Libraries installed
pip list | findstr openai
pip list | findstr python-dotenv
```

## Troubleshooting

### Python Issues
- If `python` command not found: You forgot to check "Add Python to PATH" - reinstall Python
- If pip missing: Python installation was incomplete - reinstall

### VS Code Issues
- If VS Code won't open: Try running as administrator
- Check Start menu or desktop for VS Code shortcut

### Virtual Environment Issues
- If activation fails: Check you're in the correct directory
- For PowerShell: You may need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- For Command Prompt: Use `ai-env\Scripts\activate.bat`

### Windows-Specific Notes
- Use Command Prompt OR PowerShell (both work)
- Windows uses backslashes `\` in paths
- Use `python` not `python3`
- Use `pip` not `pip3`

## Next Episode
Episode 5 starts coding! We'll create the basic command-line interface.

## Series Progress
- ✅ Episode 1: Introduction to the challenge
- ✅ Episode 2: What is technology?
- ✅ Episode 3: What tools you need
- ✅ Episode 4a: Mac installation
- 🎯 **Episode 4b: Windows installation** (You are here)
- ⏭️ Episodes 5-10: Building the chat app

## Repository Navigation
- Switch to different episodes: `git checkout episode-XX-name`
- See all episodes: `git branch -a`
- Start from scratch: `git checkout main`
