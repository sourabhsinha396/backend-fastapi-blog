from typing import List
from sqlmodel import Field, Relationship
from database.models.base import BaseModel

class User(BaseModel, table=True):
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    full_name: str
    password: str
    
    blogs: List["Blog"] = Relationship(back_populates="user")