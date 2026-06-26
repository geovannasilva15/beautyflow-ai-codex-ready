from __future__ import annotations

from sqlmodel import Session, select

from app.db.models import Service


def recommend_services(session: Session, client_profile: str, top_k: int = 3) -> list[dict]:
    profile = client_profile.lower()
    services = session.exec(select(Service).where(Service.active == True)).all()  # noqa: E712
    scored = []

    for service in services:
        haystack = f"{service.name} {service.category} {service.description} {service.tags or ''}".lower()
        score = 0
        for token in profile.split():
            if token in haystack:
                score += 1
        if "cabelo" in profile and "cabelo" in haystack:
            score += 3
        if "pele" in profile and "pele" in haystack:
            score += 3
        if "unha" in profile and "unha" in haystack:
            score += 3
        scored.append((score, service))

    scored.sort(key=lambda item: item[0], reverse=True)
    recommendations = []
    for score, service in scored[:top_k]:
        recommendations.append(
            {
                "id": service.id,
                "name": service.name,
                "category": service.category,
                "description": service.description,
                "duration_minutes": service.duration_minutes,
                "price": service.price,
                "score": score,
                "reason": "Serviço compatível com o perfil informado e interesses da cliente.",
            }
        )
    return recommendations
