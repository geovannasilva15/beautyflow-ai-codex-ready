from __future__ import annotations

import streamlit as st

from frontend.api_client import api_post
from frontend.components import page_header


def render() -> None:
    page_header("Assistente IA", "Crie respostas e mensagens profissionais.")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### Mentora de gestão")
            context = st.text_input("Contexto", "salão de beleza com agenda via WhatsApp")
            question = st.text_area("Pergunta", "Como reduzir faltas nos agendamentos?")
            if st.button("Perguntar"):
                st.markdown(api_post("/ai/chat", json={"question": question, "business_context": context})["answer"])
    with col2:
        with st.container(border=True):
            st.markdown("### Mensagem para cliente")
            goal = st.text_input("Objetivo", "confirmar agendamento")
            profile = st.text_input("Perfil", "cliente recorrente")
            tone = st.text_input("Tom", "profissional e acolhedor")
            if st.button("Gerar mensagem"):
                st.success(api_post("/ai/message", json={"goal": goal, "client_profile": profile, "tone": tone})["message"])
