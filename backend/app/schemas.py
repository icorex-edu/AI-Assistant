from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    user_id: str
    message: str
    channel: str = "web"


class ChatResponse(BaseModel):
    reply: str


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_at: Optional[str] = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_at: Optional[str] = None
    status: str
    approved: bool
