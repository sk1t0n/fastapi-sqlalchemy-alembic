from typing import Optional, List

from pydantic import BaseModel, EmailStr

from .items import Item


# Общие свойства
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None


# Свойства для получения через API при создании пользователя
class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str


# Свойства для получения через API при обновлении пользователя
class UserUpdate(UserBase):
    password: Optional[str] = None


# Общие свойства для моделей, хранящиеся в БД
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Свойства для возврата клиенту
class User(UserInDBBase):
    is_active: bool
    is_superuser: bool
    items: List[Item] = []


# Дополнительные свойства, хранящиеся в БД
class UserInDB(UserInDBBase):
    password: str
