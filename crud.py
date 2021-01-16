from typing import List, Optional

from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_users(db: Session, skip: int, limit: int) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def read_user(db: Session, id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == id).first()


def read_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def update_user(
    db: Session, user: models.User, user_schema: schemas.UserUpdate
) -> models.User:
    data_to_update = user_schema.dict(skip_defaults=True)
    for attr in data_to_update:
        if hasattr(user, attr):
            setattr(user, attr, data_to_update[attr])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: models.User) -> None:
    result = db.delete(user)
    db.commit()
    print(result)
    return result


def read_items(db: Session, skip: int, limit: int) -> List[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(
    db: Session, user_id: int, item: schemas.ItemCreate
) -> models.Item:
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
