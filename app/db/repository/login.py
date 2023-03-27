from sqlalchemy.orm import Session

from app.db.models.users import User


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
