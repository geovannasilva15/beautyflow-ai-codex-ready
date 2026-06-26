from __future__ import annotations

import streamlit as st

from frontend.styles import apply_login_styles

DEMO_USERS = {
    "geovanna@beautyflow.ai": {"password": "123456", "name": "Geovanna Silva", "role": "Fundadora"},
    "admin@beautyflow.ai": {"password": "123456", "name": "Admin BeautyFlow", "role": "Administrador"},
}


def init_auth_state() -> None:
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user" not in st.session_state:
        st.session_state.user = None


def login_user(email: str, password: str) -> bool:
    user = DEMO_USERS.get(email.strip().lower())
    if user and user["password"] == password:
        st.session_state.authenticated = True
        st.session_state.user = {"email": email.strip().lower(), "name": user["name"], "role": user["role"]}
        return True
    return False


def logout_user() -> None:
    st.session_state.authenticated = False
    st.session_state.user = None
    st.rerun()


def render_login_page() -> None:
    apply_login_styles()
    st.markdown("<h1 style='text-align:center;'>💎 BeautyFlow AI</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;color:#6d607e;'>Gestão inteligente para beleza, agenda, campanhas e atendimento com IA.</p>",
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.markdown("## Entrar no painel")
        st.caption("Acesse sua central BeautyFlow AI.")
        with st.form("login_form"):
            email = st.text_input("E-mail", value="geovanna@beautyflow.ai")
            password = st.text_input("Senha", value="123456", type="password")
            if st.form_submit_button("Entrar"):
                if login_user(email, password):
                    st.success("Login realizado com sucesso.")
                    st.rerun()
                st.error("E-mail ou senha incorretos.")
        st.info("**Acesso demo**\n\nE-mail: geovanna@beautyflow.ai  \nSenha: 123456")
