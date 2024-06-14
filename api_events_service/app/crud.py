from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict(), created_at=datetime.now())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Event).offset(skip).limit(limit).all()
