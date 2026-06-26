from __future__ import annotations


def generate_ai_answer(question: str, business_context: str) -> str:
    question_clean = question.strip()
    context_clean = business_context.strip()
    return (
        "Como assistente do BeautyFlow AI, minha sugestão é organizar essa situação em três passos: "
        "1) entender a necessidade da cliente, 2) oferecer uma resposta objetiva e acolhedora, "
        "3) transformar a conversa em ação, como agendamento, campanha ou acompanhamento.\n\n"
        f"Contexto considerado: {context_clean}\n\n"
        f"Pergunta analisada: {question_clean}\n\n"
        "Ação recomendada: registre o contato no sistema, confirme disponibilidade na agenda e envie uma mensagem curta pelo WhatsApp."
    )


def generate_client_message(goal: str, client_profile: str, tone: str) -> str:
    return (
        f"Oi, tudo bem? Passando para falar sobre {goal}. "
        f"Pensei em você porque seu perfil combina com essa sugestão: {client_profile}. "
        f"Mensagem em tom {tone}. Posso te ajudar a reservar um horário?"
    )


def generate_marketing_post(service_name: str, target_audience: str, campaign_goal: str) -> str:
    return (
        f"✨ {service_name} no BeautyFlow!\n\n"
        f"Essa campanha é ideal para {target_audience}.\n"
        f"Objetivo: {campaign_goal}.\n\n"
        "Agende seu horário e viva uma experiência de cuidado, beleza e bem-estar. 💎"
    )
