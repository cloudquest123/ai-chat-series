from openai import OpenAI  # Connect to ChatGPT
import os  # Read environment variables
from dotenv import load_dotenv  # Load API key from .env file

# Load environment variables - keeps API key secure and separate from code
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Create AI client

def get_ai_response(user_message):
    """Send user message to OpenAI and get intelligent response"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Which AI model to use
            messages=[{"role": "user", "content": user_message}],  # Format message
            max_tokens=150  # Limit response length
        )
        return response.choices[0].message.content  # Extract AI's reply
    except Exception as e:
        return f"Error: {e}"  # Handle errors gracefully

print("🤖 Bare Minimum AI Chat")
print("Type 'quit' to exit")

while True:  # Continuous conversation loop
    user_input = input("\nYou: ").strip()
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Goodbye!")
        break
    if not user_input:  # Skip empty inputs
        continue

    ai_response = get_ai_response(user_input)  # Call OpenAI API
    print(f"AI: {ai_response}")  # Print intelligent response
