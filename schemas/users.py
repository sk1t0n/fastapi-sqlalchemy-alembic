from typing import List, Optional

from pydantic import BaseModel

from .items import Item


class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
