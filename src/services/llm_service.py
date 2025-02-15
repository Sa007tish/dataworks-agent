import requests
import os

class LLMService:
    def __init__(self):
        self.token = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjIwMDA4NTJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.JoVgmQ43_Fmmd7ujrUfuF9IBm27dA_xVFdfee68Gde8'
        self.base_url = 'http://aiproxy.sanand.workers.dev/openai/v1'

    async def generate(self, prompt: str) -> str:
        response = requests.post(
            f'{self.base_url}/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.token}'
            },
            json={
                'model': 'gpt-4o-mini',
                'messages': [{'role': 'user', 'content': prompt}]
            }
        )
        return response.json()['choices'][0]['message']['content']
