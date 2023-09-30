import uuid

from fastapi_users import schemas
from pydantic import Field, BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserRead(schemas.BaseUser[uuid.UUID]):
    firstname: str = Field(max_length=25)


class UserCreate(schemas.BaseUserCreate):
    firstname: str = Field(max_length=25)


class UserUpdate(schemas.BaseUserUpdate):
    firstname: str | None = Field(max_length=25)
