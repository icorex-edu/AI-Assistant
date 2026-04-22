import httpx
from ..config import settings


class WhatsAppService:
    async def send_text(self, to_phone: str, body: str) -> dict:
        if not settings.WHATSAPP_ACCESS_TOKEN or not settings.WHATSAPP_PHONE_NUMBER_ID:
            return {"status": "not_configured", "message": "WhatsApp settings missing."}

        url = f"https://graph.facebook.com/v23.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": to_phone,
            "type": "text",
            "text": {"body": body},
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, headers=headers, json=payload)
            return {"status_code": response.status_code, "data": response.json()}
