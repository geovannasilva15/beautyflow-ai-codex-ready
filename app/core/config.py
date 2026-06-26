from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = "BeautyFlow AI"
    api_prefix: str = "/api"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///beautyflow_ai.db")
    cors_origins: tuple[str, ...] = (
        "http://localhost:8501",
        "http://127.0.0.1:8501",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
