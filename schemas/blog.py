from typing import Optional
from pydantic import BaseModel, Field, model_validator
from .user import ShowUser


class CreateBlog(BaseModel):
    title: str = Field(max_length=200)
    slug: str = Field(max_length=200)
    content: str

    @model_validator(mode="before")
    @classmethod
    def generate_slug_from_title(cls, data: dict) -> dict:
        if "title" in data:
            data["slug"] = data["title"].lower().replace(" ", "-")
        return data


class ShowBlog(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    is_active: bool
    user_id: int
    user: Optional[ShowUser] = None