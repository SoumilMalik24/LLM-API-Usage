import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    token = os.getenv("HF_API_TOKEN")
)


response = client.chat_completion(
    model = "Qwen/Qwen2.5-72B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "Help me understand AI in simple terms."}
    ]
)
print(response.choices[0].message.content)

