#!/usr/bin/env python3
"""
Episode 6: Connecting to OpenAI (API test only)
Simple API connection test - not a full application yet
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_openai_connection():
    """Test the OpenAI API connection with a simple request"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello! Can you respond with just 'Connection successful!'?"}
            ],
            max_tokens=50
        )
        
        ai_response = response.choices[0].message.content
        print("API Test Result:")
        print(f"AI Response: {ai_response}")
        return True
        
    except Exception as e:
        print(f"Error connecting to OpenAI: {e}")
        return False

def main():
    """Main function to test API connection"""
    print("OpenAI API Connection Test")
    print("-" * 30)
    
    if test_openai_connection():
        print("\n✅ OpenAI API connection successful!")
    else:
        print("\n❌ OpenAI API connection failed!")
        print("Please check:")
        print("1. Your API key in .env file")
        print("2. Your internet connection")
        print("3. Your OpenAI account has credits")

if __name__ == "__main__":
    main()