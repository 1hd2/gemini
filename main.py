import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1]
message = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

def main():
    if len(sys.argv) < 2:
        print("Provide a prompt as an arugment to main.")
        exit(1)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=message
        )
    
    print(response.text)
    
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
