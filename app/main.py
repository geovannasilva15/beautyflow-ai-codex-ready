from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import get_settings
from app.db.database import create_db_and_tables

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="API do BeautyFlow AI para gestão de beleza, agenda, campanhas e agente de atendimento.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=list(settings.cors_origins) + ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


app.include_router(router, prefix=settings.api_prefix)
