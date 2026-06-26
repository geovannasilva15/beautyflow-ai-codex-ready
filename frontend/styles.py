from __future__ import annotations

import streamlit as st


def apply_global_styles() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
            html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(236,72,153,0.12), transparent 30%),
                    radial-gradient(circle at top right, rgba(139,92,246,0.13), transparent 30%),
                    linear-gradient(180deg, #fcfbff 0%, #f8f5fb 50%, #ffffff 100%);
            }
            .block-container { max-width: 1360px !important; padding-top: 1.3rem !important; padding-bottom: 2rem !important; }
            header[data-testid="stHeader"] { background: transparent !important; }
            [data-testid="stToolbar"], [data-testid="stStatusWidget"], footer, #MainMenu { display: none !important; visibility: hidden !important; }
            section[data-testid="stSidebar"] { background: linear-gradient(180deg, #170f22 0%, #281737 55%, #42204d 100%); }
            section[data-testid="stSidebar"] * { color: #ffffff !important; }
            .stButton > button {
                border-radius: 14px !important; border: none !important;
                background: linear-gradient(135deg, #ec4899, #8b5cf6) !important;
                color: white !important; font-weight: 800 !important;
                box-shadow: 0 12px 30px rgba(236,72,153,0.22) !important;
            }
            div[data-testid="stMetric"] {
                background: rgba(255,255,255,0.86); border: 1px solid rgba(236,72,153,0.12);
                border-radius: 20px; padding: 16px; box-shadow: 0 18px 50px rgba(97,58,139,0.08);
            }
            div[data-testid="stVerticalBlockBorderWrapper"] {
                border-radius: 24px !important; background: rgba(255,255,255,0.90) !important;
                box-shadow: 0 18px 55px rgba(97,58,139,0.08) !important;
                border: 1px solid rgba(236,72,153,0.12) !important;
            }
            div[data-testid="stDataFrame"] { border-radius: 18px; overflow: hidden; }
            .hero-card {
                padding: 34px; border-radius: 30px; border: 1px solid rgba(236,72,153,0.16);
                background: radial-gradient(circle at top right, rgba(236,72,153,0.23), transparent 28%), linear-gradient(135deg,#fff,#fff0fa);
                box-shadow: 0 22px 70px rgba(97,58,139,0.12); margin-bottom: 22px;
            }
            .hero-title { font-size: clamp(2.5rem, 5vw, 5rem); line-height: .95; letter-spacing: -.075em; font-weight: 900; color: #1f1630; }
            .gradient-text { background: linear-gradient(135deg,#ec4899,#8b5cf6,#6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .badge { display:inline-flex; padding: 7px 12px; border-radius:999px; background:#fce7f3; color:#be185d; font-weight:800; font-size:.8rem; margin: 4px 6px 4px 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_login_styles() -> None:
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] { display: none !important; }
            .block-container { max-width: 520px !important; padding-top: 5rem !important; }
            .stButton > button { width: 100% !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
