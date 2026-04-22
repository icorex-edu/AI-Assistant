from fastapi import APIRouter
from ..schemas import ChatRequest, ChatResponse
from ..services.anthropic_service import ClaudeService

router = APIRouter(prefix="/chat", tags=["chat"])
claude_service = ClaudeService()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = await claude_service.generate_reply(request.message)
    return ChatResponse(reply=reply)
