from fastapi import APIRouter
from apps.v1.blog import router as blog_router


app_router = APIRouter()

app_router.include_router(blog_router, prefix="/blogs", tags=["blogs app"])
