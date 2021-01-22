from typing import Optional

from pydantic import BaseModel, EmailStr


# Общие свойства
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
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
    pass


# Дополнительные свойства, хранящиеся в БД
class UserInDB(UserInDBBase):
    hashed_password: str
