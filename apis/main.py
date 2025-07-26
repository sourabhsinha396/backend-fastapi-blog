from fastapi import APIRouter
from apis.v1.user import router as user_router
from apis.v1.blog import router as blog_router
from apis.v1.auth import api_router as auth_router

api_router = APIRouter()


api_router.include_router(user_router, prefix="/api/v1", tags=["users"])
api_router.include_router(blog_router, prefix="/api/v1", tags=["blogs"])
api_router.include_router(auth_router, prefix="/api/v1", tags=["auth"])