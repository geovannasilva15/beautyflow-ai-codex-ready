# BeautyFlow AI

BeautyFlow AI é uma plataforma inteligente para negócios da área da beleza, estética e bem-estar. O projeto une gestão de agenda, clientes, serviços, dashboard, recomendação inteligente, campanhas e um simulador de agente de IA para atendimento via WhatsApp.

## Funcionalidades

- Login demonstrativo
- Dashboard executivo
- Cadastro e gestão de clientes
- Cadastro de serviços
- Agenda de atendimentos
- Assistente IA
- Recomendador de serviços
- Atendimento IA simulado para WhatsApp
- Campanhas e mensagens programadas simuladas

## Tecnologias

- Python
- FastAPI
- SQLModel
- SQLite
- Streamlit
- Pandas
- Requests
- Git/GitHub

## Como rodar

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Crie dados iniciais:

```powershell
python seed.py
```

Rode o backend:

```powershell
python -m uvicorn app.main:app --reload
```

Em outro terminal, rode o frontend:

```powershell
python -m streamlit run frontend\streamlit_app.py
```

Acesse:

```text
http://localhost:8501
```

## Login demo

```text
E-mail: geovanna@beautyflow.ai
Senha: 123456
```

## API local

```text
http://127.0.0.1:8000/docs
```

## Estrutura

```text
app/       Backend FastAPI
frontend/  Frontend Streamlit
data/      Dados de exemplo
knowledge_base/ Base textual inicial
docs/      Documentação do projeto
tests/     Testes mínimos
```

## Próximos passos

- Integração real com WhatsApp Business API ou provedor externo
- Banco PostgreSQL em cloud
- Autenticação real
- Deploy no Render + Streamlit Community Cloud
- Melhorias no agente de IA com LLM e RAG
