import typing
import uuid

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.api.schemas.todo import TodoSchema
from src.adapter.database.models.base import Base

if typing.TYPE_CHECKING:
    from src.adapter.database.models.auth import User

UUID_ID = uuid.UUID


class Todo(Base):
    __tablename__ = 'todo'

    if typing.TYPE_CHECKING:  # pragma: no cover
        id: UUID_ID
        task: str
        description: str
        user_id: int
        done: bool
        user: User
    else:
        id: Mapped[UUID_ID] = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
        task: Mapped[str] = mapped_column(String(length=50))
        description: Mapped[str] = mapped_column(Text(), nullable=True)
        user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
        done: Mapped[bool]
        user: Mapped['User'] = relationship(back_populates='todo_list')

    def __str__(self):
        return self.task

    def read_model(self):
        return TodoSchema(
            id=self.id,
            task=self.task,
            description=self.description,
            user_id=self.user_id,
            done=self.done,
            user=self.user
        )
