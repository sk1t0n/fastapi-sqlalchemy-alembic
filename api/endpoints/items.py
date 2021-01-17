from typing import List

from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from ..dependencies import get_db
from core.config import ITEMS_PER_PAGE
from crud.item import crud_item
from schemas.items import Item, ItemCreate
from .users import find_user

router = APIRouter()


@router.get("/", response_model=List[Item], summary="Read items")
def read_items(skip: int = 0,
               limit: int = ITEMS_PER_PAGE,
               db: Session = Depends(get_db)):
    return crud_item.read_all(db, skip, limit)


@router.post("/{user_id}",
             response_model=Item,
             status_code=status.HTTP_201_CREATED,
             summary="Create item for user",
             description="Create item for user with id user_id")
def create_item_for_user(user_id: int,
                         item: ItemCreate,
                         db: Session = Depends(get_db)):
    find_user(db, user_id)
    return crud_item.create_item_for_user(db, user_id, item)
