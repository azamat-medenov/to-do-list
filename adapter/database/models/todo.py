from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

import sys

sys.path.append('..')

from .base import Base


class Todo(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(length=100))
    owner: Mapped[int] = ForeignKey('user.id')

    def __str__(self):
        return self.task


