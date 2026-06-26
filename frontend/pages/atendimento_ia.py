from __future__ import annotations

import pandas as pd
import streamlit as st

from frontend.api_client import api_get, api_post
from frontend.components import page_header


def render() -> None:
    page_header("Atendimento IA", "Simulador de WhatsApp para agendar, cancelar e responder clientes.")
    with st.container(border=True):
        st.markdown("### Nova mensagem recebida")
        c1, c2 = st.columns(2)
        name = c1.text_input("Nome da cliente", "Cliente BeautyFlow")
        phone = c2.text_input("Telefone", "11999990009")
        message = st.text_area("Mensagem da cliente", "Oi, quero marcar limpeza de pele amanhã às 14h")
        if st.button("Enviar para agente IA"):
            result = api_post("/whatsapp/simulate", json={"client_name": name, "client_phone": phone, "message": message})
            st.success(result["response"])
            st.write(f"**Intenção detectada:** {result['intent']}")
            st.write(f"**Status da ação:** {result['action_status']}")
            if result.get("appointment_id"):
                st.write(f"**Agendamento ID:** {result['appointment_id']}")
    st.write("")
    with st.container(border=True):
        st.markdown("### Histórico de conversas")
        df = pd.DataFrame(api_get("/conversations"))
        if df.empty:
            st.info("Nenhuma conversa registrada.")
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)
