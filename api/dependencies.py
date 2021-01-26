from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from core.config import API_V1_STR, ALGORITHM, SECRET_KEY
from crud.user import crud_user
from db import Session
from models.user import User
from schemas.tokens import TokenData

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.JWTError:
        raise credentials_exception
    user = crud_user.read_by_username(db, token_data.username)
    if not user:
        raise credentials_exception
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    if not crud_user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: User = Depends(get_current_user)
) -> User:
    if not crud_user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
