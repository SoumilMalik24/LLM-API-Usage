from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def stream_gemini(prompt: str):
    print("\n--- Gemini Streaming Response ---\n")

    stream = client.models.generate_content_stream(
        model = "gemini-2.5-flash",
        contents = prompt,
        config={
            "temperature": 0.3,
            "top_p": 0.9,
            "max_output_tokens": 200
        }
    )

    for chunk in stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)

if __name__ == "__main__":
    user_prompt = input("Enter prompt for Gemini: ")
    stream_gemini(user_prompt)