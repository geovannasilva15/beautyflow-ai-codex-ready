from __future__ import annotations

from sqlmodel import Session, select

from app.db.database import create_db_and_tables, engine
from app.db.models import Client, Professional, Service
from data.sample_data import SAMPLE_CLIENTS, SAMPLE_PROFESSIONALS, SAMPLE_SERVICES


def seed() -> None:
    create_db_and_tables()
    with Session(engine) as session:
        if not session.exec(select(Client)).first():
            for item in SAMPLE_CLIENTS:
                session.add(Client(**item))
        if not session.exec(select(Service)).first():
            for item in SAMPLE_SERVICES:
                session.add(Service(**item))
        if not session.exec(select(Professional)).first():
            for item in SAMPLE_PROFESSIONALS:
                session.add(Professional(**item))
        session.commit()
    print("BeautyFlow AI: dados iniciais criados com sucesso.")


if __name__ == "__main__":
    seed()
