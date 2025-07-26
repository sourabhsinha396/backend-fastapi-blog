from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from apis.deps import get_db
from core.security import create_access_token
from database.crud.user import get_user_by_email

api_router = APIRouter()


@api_router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(form_data.username, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not form_data.password == user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}