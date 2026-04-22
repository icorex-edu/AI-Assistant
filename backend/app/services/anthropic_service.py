import httpx
from ..config import settings


class ClaudeService:
    def __init__(self):
        self.api_key = settings.ANTHROPIC_API_KEY
        self.model = settings.ANTHROPIC_MODEL
        self.base_url = "https://api.anthropic.com/v1/messages"

    async def generate_reply(self, user_message: str) -> str:
        if not self.api_key:
            return (
                "Claude API key is not configured yet. "
                "Add ANTHROPIC_API_KEY in infra/.env to enable AI responses."
            )

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        payload = {
            "model": self.model,
            "max_tokens": 400,
            "system": (
                "You are an executive assistant. "
                "Be concise, helpful, and ask for approval before sending messages or posting publicly."
            ),
            "messages": [
                {"role": "user", "content": user_message}
            ],
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

        parts = data.get("content", [])
        texts = [p.get("text", "") for p in parts if p.get("type") == "text"]
        return "\n".join(texts).strip() or "No response returned."
