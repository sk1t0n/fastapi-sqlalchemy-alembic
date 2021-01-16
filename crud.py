from typing import List, Optional, Generic, TypeVar, Type

from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base
import models
import schemas

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def create(self, db: Session, obj: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def read(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def read_all(self, db: Session, skip: int, limit: int) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(
        self, db: Session, db_obj: ModelType, obj: UpdateSchemaType
    ) -> ModelType:
        data_to_update = obj.dict(skip_defaults=True)
        for attr in data_to_update:
            if hasattr(db_obj, attr):
                setattr(db_obj, attr, data_to_update[attr])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: ModelType) -> None:
        result = db.delete(db_obj)
        db.commit()
        return result


class CRUDUser(CRUDBase[models.User, schemas.UserCreate, schemas.UserUpdate]):
    def read_by_email(self, db: Session, email: str) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.email == email).first()


class CRUDItem(CRUDBase[models.Item, schemas.ItemCreate, schemas.ItemUpdate]):
    def create_item_for_user(
        self, db: Session, user_id: int, item: schemas.ItemCreate
    ) -> models.Item:
        db_item = models.Item(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


crud_user = CRUDUser(models.User)
crud_item = CRUDItem(models.Item)
