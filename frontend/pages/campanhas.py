from __future__ import annotations

from datetime import datetime, time, timedelta

import pandas as pd
import streamlit as st

from frontend.api_client import api_get, api_post
from frontend.components import page_header


def render() -> None:
    page_header("Campanhas", "Programe promoções, horários vagos e mensagens de relacionamento.")

    with st.container(border=True):
        st.markdown("### Criar campanha")
        c1, c2, c3 = st.columns([0.4, 0.3, 0.3])
        title = c1.text_input("Título", "Promoção de hidratação")
        audience = c2.text_input("Público-alvo", "cabelo")
        status = c3.selectbox("Status", ["scheduled", "draft", "sent", "canceled"], index=0)

        date = c1.date_input("Data de envio", value=datetime.now().date() + timedelta(days=1))
        hour = c2.time_input("Horário", value=time(9, 0))
        message = st.text_area(
            "Mensagem",
            "Oi, tudo bem? Essa semana temos uma condição especial para hidratação profunda. Quer reservar um horário?",
            height=130,
        )

        if st.button("Programar campanha e simular envio"):
            campaign = api_post(
                "/campaigns",
                json={
                    "title": title,
                    "message": message,
                    "target_audience": audience or None,
                    "scheduled_at": datetime.combine(date, hour).isoformat(),
                    "status": status,
                },
            )
            result = api_post(f"/campaigns/{campaign['id']}/simulate-send")
            st.success(result.get("message", "Campanha criada com sucesso."))

    st.write("")
    col1, col2 = st.columns([0.58, 0.42])

    with col1:
        st.markdown("### Campanhas cadastradas")
        campaigns = pd.DataFrame(api_get("/campaigns"))
        if campaigns.empty:
            st.info("Nenhuma campanha criada ainda.")
        else:
            st.dataframe(campaigns, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("### Mensagens simuladas")
        try:
            scheduled = pd.DataFrame(api_get("/scheduled-messages"))
        except Exception:
            scheduled = pd.DataFrame()

        if scheduled.empty:
            st.info("Nenhuma mensagem programada ainda.")
        else:
            st.dataframe(scheduled, use_container_width=True, hide_index=True)

    with st.container(border=True):
        st.markdown("### Ideias rápidas de campanhas")
        st.write("• Horário vago: avisar clientes interessadas quando abrir um encaixe no dia.")
        st.write("• Pós-atendimento: enviar mensagem de cuidado e convite para retorno.")
        st.write("• Promoção segmentada: filtrar clientes por interesse, como cabelo, pele ou sobrancelha.")
