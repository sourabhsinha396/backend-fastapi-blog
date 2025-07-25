from sqlmodel import Session
from fastapi import APIRouter, Depends, status
from apis.deps import get_db
from database.crud.user import insert_user
from schemas.user import UserCreate, ShowUser

router = APIRouter()


@router.post("/users", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return insert_user(user, db)
