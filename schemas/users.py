from typing import Optional

from pydantic import BaseModel, EmailStr


# Общие свойства
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


# Свойства для получения через API при создании пользователя
class UserCreate(UserBase):
    email: EmailStr
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


# Дополнительные свойства, хранящиеся в БД
class UserInDB(UserInDBBase):
    hashed_password: str
