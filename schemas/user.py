from pydantic import BaseModel, Field, field_validator
from sqlmodel import SQLModel


class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=255)
    email: str = Field(..., min_length=5, max_length=255)
    password: str = Field(..., min_length=4, max_length=50)

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Email must contain @')
        return v
    

class ShowUser(SQLModel):
    id: int
    full_name: str
    email: str