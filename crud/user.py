from typing import Optional

from sqlalchemy.orm import Session

from .base import CRUDBase
from core.security import get_password_hash, verify_password
from models.user import User
from schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def read_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, user: UserCreate) -> User:
        db_user = User(
            email=user.email,
            password=get_password_hash(user.password),
            full_name=user.full_name
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, db_user: User, user: UserUpdate) -> User:
        data_to_update = user.dict(exclude_unset=True)
        if data_to_update["password"]:
            hashed_password = get_password_hash(data_to_update["password"])
            data_to_update["password"] = hashed_password
        data_to_update = UserUpdate(**data_to_update)
        return super().update(db, db_user, data_to_update)

    def authenticate(
        self, db: Session, email: str, password: str
    ) -> Optional[User]:
        user = self.read_by_email(db, email)
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


crud_user = CRUDUser(User)
