#!/usr/bin/env python3
"""
Episode 5: Bare Minimum CLI Application (No AI yet)
The simplest possible CLI app - just input/output loop
"""

def main():
    """Main CLI loop - no AI, just echo functionality"""
    print("Simple CLI App")
    print("Type 'quit' to exit")
    print("-" * 30)
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Simple echo response (no AI)
        print(f"Echo: {user_input}")

if __name__ == "__main__":
    main()