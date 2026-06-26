from __future__ import annotations

from datetime import datetime, time, timedelta
import pandas as pd
import streamlit as st

from frontend.api_client import api_get, api_post, format_currency
from frontend.components import page_header


def render() -> None:
    page_header("Agenda", "Crie e visualize agendamentos.")
    clients, services, pros = api_get("/clients"), api_get("/services"), api_get("/professionals")
    appointments = api_get("/appointments")
    if clients and services and pros:
        cm = {f"{c['name']} · {c['id']}": c for c in clients}
        sm = {f"{s['name']} · {format_currency(s['price'])}": s for s in services}
        pm = {f"{p['name']} · {p['specialty']}": p for p in pros}
        with st.form("appointment_create"):
            c1, c2, c3 = st.columns(3)
            client_key = c1.selectbox("Cliente", list(cm))
            service_key = c2.selectbox("Serviço", list(sm))
            pro_key = c3.selectbox("Profissional", list(pm))
            date = c1.date_input("Data", value=datetime.now().date() + timedelta(days=1))
            hour = c2.time_input("Horário", value=time(14, 0))
            price = c3.number_input("Preço", min_value=0.0, value=float(sm[service_key]["price"]))
            if st.form_submit_button("Agendar"):
                api_post("/appointments", json={"client_id": cm[client_key]["id"], "service_id": sm[service_key]["id"], "professional_id": pm[pro_key]["id"], "scheduled_at": datetime.combine(date, hour).isoformat(), "final_price": price})
                st.success("Agendamento criado.")
                st.rerun()
    else:
        st.warning("Cadastre clientes, serviços e profissionais antes de agendar.")

    df = pd.DataFrame(appointments)
    if df.empty:
        st.info("Nenhum agendamento.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)
