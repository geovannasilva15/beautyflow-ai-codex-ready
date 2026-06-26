from __future__ import annotations

import os
from typing import Any

import requests
import streamlit as st


def get_api_url() -> str:
    try:
        api_url = st.secrets.get("API_URL")
        if api_url:
            return str(api_url).rstrip("/")
    except Exception:
        pass
    return os.getenv("API_URL", "http://127.0.0.1:8000/api").rstrip("/")


API_URL = get_api_url()


def api_get(path: str) -> Any:
    response = requests.get(f"{API_URL}{path}", timeout=20)
    response.raise_for_status()
    return response.json()


def api_post(path: str, json: dict | None = None, params: dict | None = None) -> Any:
    response = requests.post(f"{API_URL}{path}", json=json, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def api_put(path: str, json: dict | None = None) -> Any:
    response = requests.put(f"{API_URL}{path}", json=json, timeout=60)
    response.raise_for_status()
    return response.json()


def api_patch(path: str, json: dict | None = None) -> Any:
    response = requests.patch(f"{API_URL}{path}", json=json, timeout=60)
    response.raise_for_status()
    return response.json()


def api_delete(path: str) -> Any:
    response = requests.delete(f"{API_URL}{path}", timeout=60)
    response.raise_for_status()
    return response.json()


def api_online() -> bool:
    try:
        api_get("/health")
        return True
    except Exception:
        return False


def format_currency(value: float | int | None) -> str:
    value = float(value or 0)
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
