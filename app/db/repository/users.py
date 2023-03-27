from sqlalchemy.orm import Session

from app.schemas.users import UserCreate
from app.db.models.users import User
from app.core.hashing import Hashing


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hashing.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user