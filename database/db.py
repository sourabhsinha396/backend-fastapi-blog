from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

print(f"DATABASE_URL is: {settings.DATABASE_URL}")

engine = create_engine(settings.DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session