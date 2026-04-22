import httpx
from ..config import settings


class FacebookPageService:
    async def publish_post(self, message: str) -> dict:
        if not settings.FB_PAGE_ACCESS_TOKEN or not settings.FB_PAGE_ID:
            return {"status": "not_configured", "message": "Facebook Page settings missing."}

        url = f"https://graph.facebook.com/{settings.FB_PAGE_ID}/feed"
        payload = {
            "message": message,
            "access_token": settings.FB_PAGE_ACCESS_TOKEN,
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, data=payload)
            return {"status_code": response.status_code, "data": response.json()}
