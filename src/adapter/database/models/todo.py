from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapter.database.models.base import Base
from src.adapter.database.models.auth import User


class Todo(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(length=50))
    description: Mapped[str] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    done: Mapped[bool]

    user: Mapped[User] = relationship(back_populates='todo_list')

    def __str__(self):
        return self.task


