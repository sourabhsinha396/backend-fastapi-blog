import jwt
from datetime import datetime, timedelta, timezone
from core.config import settings


def create_access_token(subject: str, expires_delta_minutes: int = 60*24*15) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta_minutes)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
