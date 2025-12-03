import asyncio
import httpx

class AISession:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        self.api_url = "https://api.openai.com/v1/chat/completions"

    async def ask(self, prompt: str, api_key: str):
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(self.api_url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()

ai_engine = AISession()
