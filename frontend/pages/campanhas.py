from __future__ import annotations

from datetime import datetime, time, timedelta
import pandas as pd
import streamlit as st

from frontend.api_client import api_get, api_post
from frontend.components import page_header


def render() -> None:
    page_header("Campanhas", "Programe promoções e mensagens para clientes.")
    with st.container(border=True):
        st.markdown("### Criar campanha")
        title = st.text_input("Título", "Promoção de hidratação")
        audience = st.text_input("Público-alvo", "cabelo")
        date = st.date_input("Data de envio", value=datetime.now().date() + timedelta(days=1))
        hour = st.time_input("Horário", value=time(9, 0))
        message = st.text_area("Mensagem", "Oi! Essa semana temos uma condição especial para hidratação profunda. Quer reservar um horário?")
        if st.button("Programar campanha"):
            payload = {"title": title, "message": message, "target_audience": audience or None, "scheduled_at": datetime.combine(date, hour).isoformat(), "status": "scheduled"}
            campaign = api_post("/campaigns", json=payload)
            result = api_post(f"/campaigns/{campaign['id']}/schedule")
            st.success(result["message"])
    st.write("")
    df = pd.DataFrame(api_get("/campaigns"))
    if df.empty:
        st.info("Nenhuma campanha criada.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)
