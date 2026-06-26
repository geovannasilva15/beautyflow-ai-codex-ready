from __future__ import annotations

import streamlit as st

from frontend.api_client import api_post, format_currency
from frontend.components import page_header


def render() -> None:
    page_header("Recomendador", "Sugira serviços pelo perfil da cliente.")
    profile = st.text_area("Perfil", "Cliente com cabelo ressecado busca brilho e redução de frizz.")
    top_k = st.slider("Quantidade", 1, 5, 3)
    if st.button("Recomendar"):
        items = api_post("/recommendations", json={"client_profile": profile, "top_k": top_k})["recommendations"]
        for item in items:
            with st.container(border=True):
                st.markdown(f"### {item['name']}")
                st.write(item["description"])
                st.write(f"**Preço:** {format_currency(item['price'])}")
                st.caption(item["reason"])
