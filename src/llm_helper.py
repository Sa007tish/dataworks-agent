import requests
import os

def call_llm(prompt: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(
        "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers=headers,
        json=data
    )
    return response.json()
