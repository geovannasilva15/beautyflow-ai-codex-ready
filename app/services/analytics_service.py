from __future__ import annotations

from collections import Counter

from sqlmodel import Session, select

from app.db.models import Appointment, AppointmentStatus, Client, Service


def get_dashboard_metrics(session: Session) -> dict:
    clients = session.exec(select(Client)).all()
    appointments = session.exec(select(Appointment)).all()
    services = session.exec(select(Service)).all()
    service_by_id = {service.id: service for service in services}

    completed = [a for a in appointments if a.status == AppointmentStatus.completed]
    scheduled = [a for a in appointments if a.status == AppointmentStatus.scheduled]
    no_show = [a for a in appointments if a.status == AppointmentStatus.no_show]

    revenue = sum(a.final_price or 0 for a in completed)
    average_ticket = revenue / len(completed) if completed else 0
    no_show_rate = len(no_show) / len(appointments) if appointments else 0

    top_counter = Counter()
    for appt in appointments:
        service = service_by_id.get(appt.service_id)
        if service:
            top_counter[service.name] += 1

    top_services = [
        {"service": name, "count": count}
        for name, count in top_counter.most_common(5)
    ]

    return {
        "total_clients": len(clients),
        "total_appointments": len(appointments),
        "completed_appointments": len(completed),
        "scheduled_appointments": len(scheduled),
        "estimated_revenue": revenue,
        "average_ticket": average_ticket,
        "no_show_rate": no_show_rate,
        "top_services": top_services,
    }
