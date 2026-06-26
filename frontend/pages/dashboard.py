from __future__ import annotations

import pandas as pd
import streamlit as st

from frontend.api_client import api_get, format_currency
from frontend.components import page_header


def render() -> None:
    page_header("Dashboard executivo", "Acompanhe os principais indicadores do negócio.")
    data = api_get("/dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Clientes", data["total_clients"])
    c2.metric("Agendamentos", data["total_appointments"])
    c3.metric("Receita", format_currency(data["estimated_revenue"]))
    c4.metric("Ticket médio", format_currency(data["average_ticket"]))
    st.write("")
    top = pd.DataFrame(data.get("top_services", []))
    with st.container(border=True):
        st.markdown("### Serviços mais agendados")
        if top.empty:
            st.info("Ainda não há dados suficientes.")
        else:
            st.bar_chart(top.set_index("service"))
