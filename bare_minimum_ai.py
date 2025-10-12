from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_response(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

print("🤖 Bare Minimum AI Chat")
print("Type 'quit' to exit")

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Goodbye!")
        break
    if not user_input:
        continue

    ai_response = get_ai_response(user_input)
    print(f"AI: {ai_response}")
