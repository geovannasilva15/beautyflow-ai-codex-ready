from __future__ import annotations

import pandas as pd
import streamlit as st

from frontend.api_client import api_get, api_post
from frontend.components import page_header


EXAMPLES = {
    "Agendar": "Oi, tem horário amanhã para limpeza de pele às 14h?",
    "Cancelar": "Preciso cancelar meu horário, não vou conseguir ir hoje.",
    "Reagendar": "Quero remarcar meu atendimento para outro horário.",
    "Promoção": "Tem alguma promoção de hidratação essa semana?",
    "Dúvida": "Quanto custa uma limpeza de pele?",
}


def render() -> None:
    page_header("Atendimento IA", "Simulador de WhatsApp para agendar, cancelar e responder clientes.")

    with st.container(border=True):
        st.markdown("### Nova mensagem recebida")
        c1, c2 = st.columns(2)
        name = c1.text_input("Nome da cliente", "Cliente BeautyFlow")
        phone = c2.text_input("Telefone", "11999990009")
        example = st.selectbox("Exemplo rápido", list(EXAMPLES.keys()))
        message = st.text_area("Mensagem da cliente", EXAMPLES[example], height=120)

        if st.button("Enviar para agente IA"):
            result = api_post("/whatsapp/simulate", json={"client_name": name, "client_phone": phone, "message": message})
            st.success(result["response"])

            c1, c2, c3 = st.columns(3)
            c1.metric("Intenção detectada", result.get("intent", "desconhecido"))
            c2.metric("Status da ação", result.get("action_status", "simulated"))
            c3.metric("ID do agendamento", result.get("appointment_id") or "—")

            with st.container(border=True):
                st.markdown("### Ação sugerida")
                st.write(result.get("action_suggested", "Registrar conversa e responder cliente."))

    st.write("")
    with st.container(border=True):
        st.markdown("### Histórico de conversas")
        df = pd.DataFrame(api_get("/conversations"))
        if df.empty:
            st.info("Nenhuma conversa registrada.")
        else:
            columns = ["created_at", "client_name", "client_phone", "incoming_message", "detected_intent", "ai_response", "action_status", "appointment_id"]
            available = [column for column in columns if column in df.columns]
            st.dataframe(df[available], use_container_width=True, hide_index=True)
