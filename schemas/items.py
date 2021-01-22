from typing import Optional

from pydantic import BaseModel


# Общие свойства
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Свойства для получения через API при создании элемента
class ItemCreate(ItemBase):
    title: str


# Свойства для получения через API при обновлении элемента
class ItemUpdate(ItemBase):
    pass


# Общие свойства для моделей, хранящиеся в БД
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Свойства для возврата клиенту
class Item(ItemInDBBase):
    pass


# Дополнительные свойства, хранящиеся в БД
class ItemInDB(ItemInDBBase):
    pass
