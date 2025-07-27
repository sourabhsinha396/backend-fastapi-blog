from fastapi import FastAPI
from typing import Dict
from sqlalchemy import text
from core.config import settings
from apis.deps import get_db
from apis.main import api_router
from apps.main import app_router


app: FastAPI = FastAPI(title=settings.TITLE, description=settings.DESCRIPTION, version=settings.VERSION)
app.include_router(api_router)
app.include_router(app_router)

@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get("/health/db")
def health_check_db() -> Dict[str, str]:
    try:
        db = next(get_db())
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}