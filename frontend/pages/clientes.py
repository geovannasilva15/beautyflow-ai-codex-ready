from __future__ import annotations

import pandas as pd
import streamlit as st

from frontend.api_client import api_delete, api_get, api_post, api_put
from frontend.components import page_header


def render() -> None:
    page_header("Clientes", "Cadastre, busque, edite e gerencie clientes.")
    with st.expander("Cadastrar novo cliente", expanded=True):
        with st.form("client_create"):
            c1, c2, c3 = st.columns(3)
            name = c1.text_input("Nome")
            phone = c1.text_input("Telefone")
            email = c2.text_input("E-mail")
            hair_type = c2.text_input("Tipo de cabelo")
            skin_type = c3.text_input("Tipo de pele")
            interests = c3.text_input("Interesses")
            notes = st.text_area("Observações")
            if st.form_submit_button("Salvar cliente"):
                if not name or not phone:
                    st.warning("Nome e telefone são obrigatórios.")
                else:
                    api_post("/clients", json={"name": name, "phone": phone, "email": email or None, "hair_type": hair_type or None, "skin_type": skin_type or None, "interests": interests or None, "notes": notes or None})
                    st.success("Cliente cadastrado.")
                    st.rerun()

    clients = api_get("/clients")
    df = pd.DataFrame(clients)
    if df.empty:
        st.info("Nenhum cliente cadastrado.")
        return
    search = st.text_input("Buscar cliente")
    if search:
        s = search.lower()
        df = df[df.apply(lambda row: s in " ".join(str(v).lower() for v in row.values), axis=1)]
    for _, client in df.iterrows():
        client_id = int(client["id"])
        with st.container(border=True):
            st.markdown(f"### 👤 {client['name']}")
            st.write(f"**Telefone:** {client.get('phone', '')}")
            st.write(f"**E-mail:** {client.get('email') or 'Não informado'}")
            st.write(f"**Interesses:** {client.get('interests') or 'Não informado'}")
            with st.expander("Editar"):
                with st.form(f"edit_{client_id}"):
                    name = st.text_input("Nome", value=str(client.get("name") or ""), key=f"n{client_id}")
                    phone = st.text_input("Telefone", value=str(client.get("phone") or ""), key=f"p{client_id}")
                    email = st.text_input("E-mail", value=str(client.get("email") or ""), key=f"e{client_id}")
                    interests = st.text_input("Interesses", value=str(client.get("interests") or ""), key=f"i{client_id}")
                    if st.form_submit_button("Atualizar"):
                        api_put(f"/clients/{client_id}", json={"name": name, "phone": phone, "email": email or None, "interests": interests or None})
                        st.success("Atualizado.")
                        st.rerun()
            with st.expander("Excluir"):
                if st.button("Excluir cliente", key=f"del{client_id}"):
                    try:
                        api_delete(f"/clients/{client_id}")
                        st.success("Excluído.")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Erro: {exc}")
