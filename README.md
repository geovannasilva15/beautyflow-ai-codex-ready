<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=ec4899&height=180&section=header&text=BeautyFlow%20AI&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=34&desc=Gest%C3%A3o%20inteligente%20para%20beleza%20e%20bem-estar&descAlignY=57" alt="BeautyFlow AI" />

</div>

![Visão explicativa do projeto BeautyFlow AI](assets/readme-project-overview.svg)


<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Interface-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

**Plataforma para centralizar agenda, clientes, serviços, campanhas e atendimento inteligente em negócios de beleza.**

</div>

## Sobre o projeto

O BeautyFlow AI é um protótipo full stack voltado a salões, clínicas de estética e profissionais autônomos. A aplicação combina gestão operacional, indicadores e recursos inteligentes em uma experiência integrada.

## Principais funcionalidades

- Dashboard executivo com indicadores do negócio
- Cadastro e gestão de clientes e serviços
- Agenda de atendimentos
- Assistente e recomendador de serviços
- Simulação de atendimento pelo WhatsApp
- Campanhas e mensagens programadas
- API documentada automaticamente

## Arquitetura

```mermaid
flowchart LR
    UI[Streamlit] --> API[FastAPI]
    API --> DB[(SQLite)]
    API --> ML[Recomendador]
    API --> SVC[Serviços]
```

## Tecnologias

Python, FastAPI, Streamlit, SQLModel, SQLite, Pandas, Requests, Pytest e HTTPX.

## Executar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python seed.py
python -m uvicorn app.main:app --reload
```

Em outro terminal:

```bash
python -m streamlit run frontend/streamlit_app.py
```

Acesse a interface em `http://localhost:8501` e a documentação da API em `http://127.0.0.1:8000/docs`.

<details><summary>Credenciais demonstrativas</summary>

```text
E-mail: geovanna@beautyflow.ai
Senha: 123456
```

</details>

## Estrutura

```text
app/             Backend e regras de negócio
frontend/        Interface Streamlit
data/            Dados demonstrativos
knowledge_base/  Base textual
docs/            Documentação
tests/           Testes
```

## Autoria

Desenvolvido por **[Geovanna Eduarda da Silva](https://github.com/geovannasilva15)**.
