from sqlalchemy.orm import Session

from demo.models import models
from demo.schemas import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_first_name(db: Session, first_name: str):
    return db.query(models.User).filter(models.User.first_name == first_name).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_sell_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SellPlaces).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_sell_places(db: Session, places: schemas.SellPlacesBase, user_id: int):
    db_item = models.SellPlaces(**places.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
