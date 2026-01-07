from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Explain transformers simply"}
    ]
)

print(response.output_text)