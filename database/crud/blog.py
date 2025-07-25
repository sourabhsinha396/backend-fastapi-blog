from typing import List, Optional
from sqlmodel import Session
from fastapi import Depends
from sqlmodel import select

from database.models.blog import Blog
from apis.deps import get_db
from schemas.blog import CreateBlog


def insert_blog(blog: CreateBlog, db: Session = Depends(get_db)) -> Blog:
    db_blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        is_active=True,
        user_id=1
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_blog_by_slug(slug: str, db: Session = Depends(get_db)) -> Blog:
    # return db.query(Blog).filter(Blog.slug == slug).first()  #the sqlalchemy way
    statement = select(Blog).where(Blog.slug == slug)
    result = db.exec(statement)
    return result.first()


def get_all_blogs(db: Session = Depends(get_db)) -> List[Blog]:
    statement = select(Blog)
    result = db.exec(statement)
    return result.all()


def update_blog_by_slug(slug: str, blog: CreateBlog, db: Session = Depends(get_db)) -> Blog:
    statement = select(Blog).where(Blog.slug == slug)
    result = db.exec(statement)
    db_blog = result.first()
    if not db_blog:
        return None
    db_blog.title = blog.title
    db_blog.slug = blog.slug
    db_blog.content = blog.content
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog_by_slug(slug: str, db: Session = Depends(get_db)) -> Optional[bool]:
    statement = select(Blog).where(Blog.slug == slug)
    result = db.exec(statement)
    db_blog = result.first()
    if not db_blog:
        return None
    db.delete(db_blog)
    db.commit()
    return True