from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Todo(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(length=100))
    description: Mapped[str] = mapped_column(Text())
    owner_id: Mapped[int] = ForeignKey('user.id')
    done: Mapped[bool]


    def __str__(self):
        return self.task


