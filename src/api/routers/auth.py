import uuid
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.api.schemas.auth import UserRead, UserCreate
from src.adapter.database.models.auth import User
from src.adapter.auth.manager import get_user_manager
from src.adapter.auth.backend_config import auth_backend

fastapi_users_router = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


def setup(app: FastAPI):
    app.include_router(
        fastapi_users_router.get_auth_router(auth_backend),
        prefix='/api',
        tags=['auth']
    )
    app.include_router(
        fastapi_users_router.get_register_router(UserRead, UserCreate),
        prefix='/api',
        tags=["auth"],
    )
