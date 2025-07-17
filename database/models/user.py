from typing import List
from database.models.base import BaseModel
from sqlmodel import Field, Relationship


class User(BaseModel, table=True):
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    full_name: str
    password: str
    
    # Quotes for forwared reference to Blog: Tells python to do type checking when all the classes are fully loaded
    blogs: List["Blog"] = Relationship(back_populates="user")