import typing
from typing import List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.api.schemas.auth import UserSchema
from src.adapter.database.models.base import Base

if typing.TYPE_CHECKING:
    from src.adapter.database.models.todo import Todo


class User(SQLAlchemyBaseUserTableUUID, Base):
    firstname: Mapped[str] = mapped_column(String(length=25), nullable=False)
    todo_list: Mapped[List['Todo']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )

    def read_model(self):
        return UserSchema(
            id=self.id,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_superuser=self.is_superuser,
            is_verified=self.is_verified,
            firstname=self.firstname,
            todo_list=self.todo_list
        )
