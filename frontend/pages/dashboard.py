from __future__ import annotations

import pandas as pd
import streamlit as st

from frontend.api_client import api_get, format_currency
from frontend.components import page_header


def render() -> None:
    page_header("Dashboard executivo", "Acompanhe os principais indicadores do negócio.")

    data = api_get("/dashboard")
    appointments = pd.DataFrame(api_get("/appointments"))
    clients = pd.DataFrame(api_get("/clients"))
    services = pd.DataFrame(api_get("/services"))

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Clientes", data.get("total_clients", 0))
    c2.metric("Agendamentos", data.get("total_appointments", 0))
    c3.metric("Receita estimada", format_currency(data.get("estimated_revenue", 0)))
    c4.metric("Ticket médio", format_currency(data.get("average_ticket", 0)))

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Concluídos", data.get("completed_appointments", 0))
    c6.metric("Programados", data.get("scheduled_appointments", 0))
    c7.metric("Taxa de falta", f"{float(data.get('no_show_rate', 0)) * 100:.1f}%")
    c8.metric("Serviços ativos", len(services) if not services.empty else 0)

    st.write("")
    col1, col2 = st.columns([0.55, 0.45])

    with col1:
        with st.container(border=True):
            st.markdown("### Serviços mais agendados")
            top = pd.DataFrame(data.get("top_services", []))
            if top.empty:
                st.info("Ainda não há dados suficientes.")
            else:
                st.bar_chart(top.set_index("service"))

    with col2:
        with st.container(border=True):
            st.markdown("### Próximos atendimentos")
            if appointments.empty:
                st.info("Nenhum atendimento registrado.")
            else:
                client_names = dict(zip(clients.get("id", []), clients.get("name", []))) if not clients.empty else {}
                service_names = dict(zip(services.get("id", []), services.get("name", []))) if not services.empty else {}
                upcoming = appointments.copy()
                upcoming["cliente"] = upcoming["client_id"].map(client_names)
                upcoming["serviço"] = upcoming["service_id"].map(service_names)
                upcoming = upcoming[["scheduled_at", "cliente", "serviço", "status"]].head(6)
                st.dataframe(upcoming, use_container_width=True, hide_index=True)

    with st.container(border=True):
        st.markdown("### Leitura rápida")
        st.write(
            "O BeautyFlow AI centraliza agenda, relacionamento e campanhas para ajudar o negócio a transformar "
            "conversas em atendimentos e oportunidades de venda."
        )
