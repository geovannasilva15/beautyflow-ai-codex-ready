from __future__ import annotations

import streamlit as st

from frontend.api_client import api_get, format_currency
from frontend.components import hero, page_header


def render() -> None:
    hero()
    page_header("Central inteligente do negócio", "Visão geral do BeautyFlow AI.")
    data = api_get("/dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Clientes", data["total_clients"])
    c2.metric("Agendamentos", data["total_appointments"])
    c3.metric("Receita estimada", format_currency(data["estimated_revenue"]))
    c4.metric("Ticket médio", format_currency(data["average_ticket"]))

    st.write("")
    a, b, c = st.columns(3)
    with a:
        with st.container(border=True):
            st.markdown("### 🤖 Atendimento IA")
            st.write("Simule conversas de WhatsApp, detecte intenção e crie ações na agenda.")
    with b:
        with st.container(border=True):
            st.markdown("### 📣 Campanhas")
            st.write("Programe promoções, mensagens para horários vagos e relacionamento com clientes.")
    with c:
        with st.container(border=True):
            st.markdown("### 📊 Gestão")
            st.write("Acompanhe clientes, agendamentos, serviços e indicadores do negócio.")
