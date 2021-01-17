from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from ..dependencies import get_db
from core.config import USERS_PER_PAGE
from crud.user import crud_user
from models.user import User
from schemas.users import User as UserSchema, UserCreate, UserUpdate

router = APIRouter()


@router.post("/",
             response_model=UserSchema,
             status_code=status.HTTP_201_CREATED,
             summary="Create user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.read_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create(db, user)


@router.get("/", response_model=List[UserSchema], summary="Read users")
def read_users(skip: int = 0,
               limit: int = USERS_PER_PAGE,
               db: Session = Depends(get_db)):
    return crud_user.read_all(db, skip, limit)


def find_user(db: Session, user_id: int) -> User:
    db_user = crud_user.read(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/{user_id}", response_model=UserSchema, summary="Read user")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return find_user(db, user_id)


@router.patch("/{user_id}", response_model=UserSchema, summary="Update user")
def update_user(user_id: int,
                user_schema: UserUpdate,
                db: Session = Depends(get_db)):
    db_user = find_user(db, user_id)
    return crud_user.update(db, db_user, user_schema)


@router.delete("/{user_id}",
               status_code=status.HTTP_204_NO_CONTENT,
               summary="Delete user")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = find_user(db, user_id)
    return crud_user.delete(db, db_user)
