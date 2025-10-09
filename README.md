# Episode 4a: Installing Tools - Mac Version

## Table of Contents
- [What You'll Learn](#what-youll-learn)
- [Installation Steps](#installation-steps)
- [Verification Commands](#verification-commands)
- [Troubleshooting](#troubleshooting)
- [Next Episode](#next-episode)
- [Series Progress](#series-progress)
- [Repository Navigation](#repository-navigation)

## What You'll Learn
Complete Mac installation walkthrough for Python, VS Code, and setting up your development environment.

## Installation Steps

### 1. Python Installation (Mac)
1. Go to [python.org](https://python.org)
2. Download the `.pkg` installer (not Homebrew)
3. Run the installer 
4. Use the **official installer** for best compatibility

### 2. Verify Python Installation
Open Terminal and run these commands:

```bash
# Check Python version
python3 --version

# Check pip version  
pip3 --version

# If pip is missing, run:
python3 -m ensurepip
```

You should see version numbers for both commands.

### 3. VS Code Installation (Mac)
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download the `.dmg` file
3. Open the `.dmg` file
4. Drag VS Code to your Applications folder
5. Launch VS Code from Applications

### 4. Virtual Environment Setup
Create an isolated Python environment for your project:

```bash
# Clone or create project folder
git clone https://github.com/cloudquest123/ai-chat-series.git
cd ai-chat-series

# Create virtual environment
python3 -m venv ai_project

# Activate environment (Mac)
source ai_project/bin/activate

# You should see (ai_project) in your prompt
```

### 5. Install Required Libraries
With your virtual environment active:

```bash
# Install the libraries we need
pip install openai python-dotenv

# Verify installation
pip list
```

## Verification Commands
Run these to confirm everything works:

```bash
# Python and pip working
python3 --version
pip3 --version

# Virtual environment active
echo $VIRTUAL_ENV

# Libraries installed
pip list | grep openai
pip list | grep python-dotenv
```

## Troubleshooting

### Python Issues
- If `python3` command not found: Restart Terminal after installation
- If pip missing: Run `python3 -m ensurepip`

### VS Code Issues  
- If VS Code won't open: Right-click and select "Open" to bypass security
- Make sure you dragged to Applications folder, not just opened from Downloads

### Virtual Environment Issues
- If activation fails: Check you're in the correct directory
- If prompt doesn't change: Try `which python` to verify you're in the environment

## Next Episode
Episode 5 starts coding! We'll create the basic command-line interface.

## Series Progress
- ✅ Episode 1: Introduction to the challenge
- ✅ Episode 2: What is technology?
- ✅ Episode 3: What tools you need
- 🎯 **Episode 4a: Mac installation** (You are here)
- ⏭️ Episode 4b: Windows installation  
- ⏭️ Episodes 5-10: Building the chat app

## Repository Navigation
- Switch to different episodes: `git checkout episode-XX-name`
- See all episodes: `git branch -a`
- Start from scratch: `git checkout main`
