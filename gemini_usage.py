from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def stream_response(prompt:str):
    print("\n-------Streaming Response-------\n")

    stream=client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "max_output_tokens": 1000,
            "temperature": 0.3          
        }
    )

    for chunk in stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    stream_response(user_prompt)
