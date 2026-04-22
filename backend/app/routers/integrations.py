from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import PlainTextResponse
from ..config import settings
from ..services.whatsapp_service import WhatsAppService
from ..services.facebook_service import FacebookPageService

router = APIRouter(tags=["integrations"])
whatsapp_service = WhatsAppService()
facebook_service = FacebookPageService()


@router.get("/webhooks/whatsapp")
async def verify_whatsapp_webhook(hub_mode: str = "", hub_verify_token: str = "", hub_challenge: str = ""):
    if hub_mode == "subscribe" and hub_verify_token == settings.WHATSAPP_VERIFY_TOKEN:
        return PlainTextResponse(content=hub_challenge)
    raise HTTPException(status_code=403, detail="Verification failed")


@router.post("/webhooks/whatsapp")
async def receive_whatsapp_webhook(request: Request):
    payload = await request.json()
    return {"received": True, "payload": payload}


@router.post("/integrations/whatsapp/send")
async def send_whatsapp(payload: dict):
    to_phone = payload.get("to")
    body = payload.get("body")
    return await whatsapp_service.send_text(to_phone, body)


@router.post("/integrations/facebook/post")
async def create_page_post(payload: dict):
    message = payload.get("message")
    return await facebook_service.publish_post(message)
