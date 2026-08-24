from __future__ import annotations

from sqlmodel import Session, select

from app.db.models import Campaign, Client, ScheduledMessage
from app.schemas.schemas import CampaignCreate


def create_campaign(session: Session, payload: CampaignCreate) -> Campaign:
    campaign = Campaign(**payload.model_dump())
    session.add(campaign)
    session.commit()
    session.refresh(campaign)
    return campaign


def schedule_campaign_messages(session: Session, campaign_id: int) -> dict:
    campaign = session.get(Campaign, campaign_id)
    if not campaign:
        return {"created": 0, "message": "Campanha não encontrada."}

    existing_messages = session.exec(
        select(ScheduledMessage).where(ScheduledMessage.campaign_id == campaign_id)
    ).all()
    for message in existing_messages:
        session.delete(message)
    session.commit()

    clients = session.exec(select(Client)).all()
    created = 0
    for client in clients:
        interests = (client.interests or "").lower()
        audience = (campaign.target_audience or "").lower()
        if audience and audience not in interests and audience not in client.name.lower():
            continue

        scheduled = ScheduledMessage(
            campaign_id=campaign.id,
            client_id=client.id,
            client_phone=client.phone,
            message=campaign.message,
            scheduled_at=campaign.scheduled_at,
            status="scheduled",
        )
        session.add(scheduled)
        created += 1

    session.commit()
    campaign.status = "scheduled"
    session.add(campaign)
    session.commit()

    return {"created": created, "message": f"{created} mensagens simuladas foram programadas."}
