from __future__ import annotations

import streamlit as st


def page_header(title: str, subtitle: str) -> None:
    st.markdown(f"# {title}")
    st.caption(subtitle)
    st.write("")


def hero() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <span class="badge">✨ SaaS inteligente para beleza e bem-estar</span>
            <div class="hero-title">BeautyFlow <span class="gradient-text">AI</span></div>
            <p style="color:#6d607e;max-width:780px;line-height:1.7;">
                Gestão visual para negócios de beleza com dashboard, agenda, clientes, serviços,
                agente de atendimento IA, campanhas e recomendação inteligente.
            </p>
            <span class="badge">🤖 Atendimento IA</span>
            <span class="badge">📅 Agenda</span>
            <span class="badge">📣 Campanhas</span>
            <span class="badge">🧠 Machine Learning</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
