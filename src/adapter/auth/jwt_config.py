import os

from fastapi_users.authentication import JWTStrategy
from dotenv import load_dotenv


load_dotenv()

SECRET = os.getenv('JWT_SECRET')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
