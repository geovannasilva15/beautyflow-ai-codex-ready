@echo off
cd /d %~dp0
call .venv\Scripts\activate.bat
python -m streamlit run frontend\streamlit_app.py
