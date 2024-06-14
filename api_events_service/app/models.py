from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    provider_name = Column(String, index=True)
    event_type = Column(String)
    event_data = Column(String)
    created_at = Column(DateTime)
