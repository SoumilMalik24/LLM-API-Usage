import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def stream_openai(prompt: str):
    print("\n--- OpenAi Streaming Response ---\n")
    stream = client.chat.completions.create(

        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a precise technical tutor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        top_p=0.9,
        max_tokens=200,
        stop=["\n\n"],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)


if __name__ == "__main__":
    user_prompt = input("Enter prompt for OpenAI: ")
    stream_openai(user_prompt)

    