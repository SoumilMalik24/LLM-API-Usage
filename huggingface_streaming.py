import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    model="Qwen/Qwen2.5-72B-Instruct",
    token=os.getenv("HF_API_TOKEN")
)

stream = client.chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "Explain AI like I am a beginner."}
    ],
    max_tokens=200,
    temperature=0.3,
    top_p=0.9,
    stream=True
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
