from sqlalchemy.orm import Session
from app import models, schemas

def create_api(db: Session, api: schemas.APIBase):
    db_api = models.API(name=api.name, path=api.path)
    db.add(db_api)
    db.commit()
    db.refresh(db_api)
    return db_api

def get_api(db: Session, api_id: int):
    return db.query(models.API).filter(models.API.id == api_id).first()

def get_apis(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.API).offset(skip).limit(limit).all()
