from sqlalchemy import Column, Integer, String
from app.database import Base

class API(Base):
    __tablename__ = "apis"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    path = Column(String)
