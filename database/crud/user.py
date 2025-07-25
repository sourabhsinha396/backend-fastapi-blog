from sqlmodel import Session, select
from fastapi import Depends
from database.models.user import User

from apis.deps import get_db
from schemas.user import UserCreate


def insert_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    db_user = User(
        username=user.email,
        email=user.email,
        full_name=user.full_name,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(email: str, db: Session = Depends(get_db)) -> User:
    statement = select(User).where(User.email == email)
    result = db.exec(statement)
    return result.first()