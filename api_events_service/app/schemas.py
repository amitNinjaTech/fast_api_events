from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    provider_name: str
    event_type: str
    event_data: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class EventResponse(BaseModel):
    message: str
