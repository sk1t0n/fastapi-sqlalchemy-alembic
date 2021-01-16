from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from config import USERS_PER_PAGE, ITEMS_PER_PAGE
import crud
import models
import schemas

router = APIRouter()


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.read_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@router.get("/users", response_model=List[schemas.User])
def read_users(
    skip: int = 0, limit: int = USERS_PER_PAGE, db: Session = Depends(get_db)
):
    return crud.read_users(db, skip, limit)


def find_user(db: Session, user_id: int) -> models.User:
    db_user = crud.read_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return find_user(db, user_id)


@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int, user_schema: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    db_user = find_user(db, user_id)
    return crud.update_user(db, db_user, user_schema)


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = find_user(db, user_id)
    return crud.delete_user(db, db_user)


@router.get("/users/items", response_model=List[schemas.Item])
def read_items(
    skip: int = 0, limit: int = ITEMS_PER_PAGE, db: Session = Depends(get_db)
):
    return crud.read_items(db, skip, limit)


@router.post("/users/{user_id}/items")
def create_user_item(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    find_user(db, user_id)
    return crud.create_user_item(db, user_id, item)
