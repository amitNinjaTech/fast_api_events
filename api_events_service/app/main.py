from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/events/", response_model=schemas.EventResponse)
async def receive_events(events: List[schemas.EventCreate], db: Session = Depends(get_db)):
    for event_data in events:
        crud.create_event(db, event_data)
    return {"message": f"{len(events)} events received"}

@app.get("/api/events/", response_model=List[schemas.Event])
def list_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events
