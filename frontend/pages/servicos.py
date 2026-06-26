from __future__ import annotations

import pandas as pd
import streamlit as st

from frontend.api_client import api_get, api_post, format_currency
from frontend.components import page_header


def render() -> None:
    page_header("Serviços", "Monte um catálogo para agenda, IA e recomendações.")
    with st.expander("Cadastrar serviço", expanded=True):
        with st.form("service_create"):
            c1, c2 = st.columns(2)
            name = c1.text_input("Nome")
            category = c1.text_input("Categoria")
            duration = c1.number_input("Duração", min_value=10, value=60)
            price = c2.number_input("Preço", min_value=0.0, value=100.0)
            tags = c2.text_input("Tags")
            description = st.text_area("Descrição")
            if st.form_submit_button("Salvar serviço"):
                api_post("/services", json={"name": name, "category": category, "description": description, "duration_minutes": int(duration), "price": float(price), "tags": tags or None})
                st.success("Serviço cadastrado.")
                st.rerun()
    services = pd.DataFrame(api_get("/services"))
    if services.empty:
        st.info("Nenhum serviço cadastrado.")
    else:
        services["price"] = services["price"].apply(format_currency)
        st.dataframe(services, use_container_width=True, hide_index=True)
