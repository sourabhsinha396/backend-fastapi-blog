from fastapi import FastAPI
from typing import Dict
from core.config import settings

app: FastAPI = FastAPI(title=settings.title, description=settings.description, version=settings.version)


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello World"}