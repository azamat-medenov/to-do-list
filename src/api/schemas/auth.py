import uuid
from typing import List

from fastapi_users import schemas
from pydantic import Field, BaseModel, ConfigDict

from src.api.schemas.todo import TodoSchema


class UserRead(schemas.BaseUser[uuid.UUID]):
    firstname: str = Field(max_length=25)


class UserCreate(schemas.BaseUserCreate):
    firstname: str = Field(max_length=25)


class UserUpdate(schemas.BaseUserUpdate):
    firstname: str | None = Field(max_length=25)


class UserSchema(BaseModel):
    id: uuid.UUID
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    firstname: str
    todo_list: List[TodoSchema] = []

    model_config = ConfigDict(from_attributes=True)

