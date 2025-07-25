from typing import List
from sqlmodel import Session
from fastapi import APIRouter, Depends, status, HTTPException

from apis.deps import get_db
from database.crud.blog import insert_blog, get_blog_by_slug, get_all_blogs, update_blog_by_slug, delete_blog_by_slug
from schemas.blog import CreateBlog, ShowBlog


router = APIRouter()


@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    return insert_blog(blog, db)


@router.get("/blogs/{slug}", response_model=ShowBlog)
def get_blog(slug: str, db: Session = Depends(get_db)):
    blog = get_blog_by_slug(slug, db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    return get_all_blogs(db)


@router.put("/blogs/{slug}", response_model=ShowBlog)
def update_blog(slug: str, blog: CreateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_slug(slug, blog, db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


@router.delete("/blogs/{slug}", status_code=status.HTTP_200_OK)
def delete_blog(slug: str, db: Session = Depends(get_db)):
    if delete_blog_by_slug(slug, db):
        return {"detail": "Blog deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")