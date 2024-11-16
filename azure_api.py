from openai import AzureOpenAI
from config import AZURE_API

client = AzureOpenAI(
    azure_endpoint=AZURE_API['endpoint'],
    api_key=AZURE_API['key'],
    api_version='2024-02-01'
)

def chat_ai(prompt: str):
    response = client.chat.completions.create(
        model = "gpt-35-turbo",
        messages = [
            {"role": "system", "content": "You are helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content