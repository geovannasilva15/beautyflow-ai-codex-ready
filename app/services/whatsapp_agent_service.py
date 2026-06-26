from __future__ import annotations

from sqlmodel import Session

from app.db.models import ConversationIntent, ConversationMessage
from app.services.appointment_service import cancel_latest_appointment, create_appointment_from_message


def detect_intent(message: str) -> ConversationIntent:
    text = message.lower()
    if any(word in text for word in ["cancelar", "desmarcar", "não vou", "nao vou", "remarcar"]):
        if any(word in text for word in ["remarcar", "reagendar", "outro horário", "outro horario"]):
            return ConversationIntent.reschedule
        return ConversationIntent.cancel
    if any(word in text for word in ["marcar", "agendar", "horário", "horario", "tem vaga", "disponível", "disponivel"]):
        return ConversationIntent.schedule
    if any(word in text for word in ["promo", "promoção", "promocao", "desconto", "oferta"]):
        return ConversationIntent.promotion
    if any(word in text for word in ["quanto", "valor", "preço", "preco", "serviço", "servico"]):
        return ConversationIntent.question
    return ConversationIntent.unknown


def process_whatsapp_message(session: Session, client_name: str, client_phone: str, message: str) -> dict:
    intent = detect_intent(message)
    appointment_id = None
    action_status = "responded"

    if intent == ConversationIntent.schedule:
        response, appointment_id = create_appointment_from_message(session, client_name, client_phone, message)
        action_status = "appointment_created" if appointment_id else "appointment_suggestion"
    elif intent == ConversationIntent.cancel:
        response, appointment_id = cancel_latest_appointment(session, client_phone)
        action_status = "appointment_canceled" if appointment_id else "cancel_not_found"
    elif intent == ConversationIntent.reschedule:
        response = "Claro! Posso te ajudar a reagendar. Tenho opções amanhã às 10h, 14h ou 16h. Qual fica melhor?"
        action_status = "reschedule_suggested"
    elif intent == ConversationIntent.promotion:
        response = "Temos campanhas especiais disponíveis. Posso te enviar as promoções da semana e reservar um horário para você."
    elif intent == ConversationIntent.question:
        response = "Posso te ajudar! Temos serviços de beleza, estética e bem-estar. Quer saber valores ou horários disponíveis?"
    else:
        response = "Oi! Sou a assistente do BeautyFlow AI. Posso ajudar com agendamentos, cancelamentos, valores e promoções."

    record = ConversationMessage(
        client_name=client_name,
        client_phone=client_phone,
        incoming_message=message,
        detected_intent=intent,
        ai_response=response,
        action_status=action_status,
        appointment_id=appointment_id,
    )
    session.add(record)
    session.commit()
    session.refresh(record)

    return {
        "intent": intent,
        "response": response,
        "action_status": action_status,
        "appointment_id": appointment_id,
        "conversation_id": record.id,
    }
