from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import chat, tasks, integrations

app = FastAPI(title=settings.APP_NAME)

allow_origins = ["*"] if settings.FRONTEND_ORIGIN == "*" else [settings.FRONTEND_ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "AI Executive Assistant backend is running."}


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(chat.router)
app.include_router(tasks.router)
app.include_router(integrations.router)
