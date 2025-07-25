from sqlmodel import Field, Relationship
from database.models.base import BaseModel

class Blog(BaseModel, table=True):
    title: str = Field(max_length=200)
    slug: str = Field(max_length=200, unique=True)
    content: str
    is_active: bool = Field(default=True)
    user_id: int = Field(foreign_key="user.id")
    
    user: "User" = Relationship(back_populates="blogs")