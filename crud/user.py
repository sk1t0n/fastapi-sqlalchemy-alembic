from typing import Optional

from sqlalchemy.orm import Session

from .base import CRUDBase
from models.user import User
from schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def read_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()


crud_user = CRUDUser(User)
