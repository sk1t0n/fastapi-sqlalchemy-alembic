from typing import List

from sqlalchemy.orm import Session

from .base import CRUDBase
from models.item import Item
from schemas.items import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_item_for_user(
        self, db: Session, user_id: int, item: ItemCreate
    ) -> Item:
        db_item = Item(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def read_items_for_user(self, db: Session, user_id: int) -> List[Item]:
        return db.query(Item).filter(Item.owner_id == user_id).all()


crud_item = CRUDItem(Item)
