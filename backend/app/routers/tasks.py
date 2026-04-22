from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])

FAKE_TASKS = []


@router.get("")
async def list_tasks():
    return FAKE_TASKS


@router.post("")
async def create_task(payload: dict):
    payload["id"] = len(FAKE_TASKS) + 1
    payload["status"] = "pending"
    payload["approved"] = False
    FAKE_TASKS.append(payload)
    return payload
