import os
from openai import OpenAI

def main():
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        print("Error: OPENAI_KEY environment variable not set")
        return

    client = OpenAI(api_key=api_key)
    print("OpenAI client initialized successfully!")

if __name__ == "__main__":
    main() 