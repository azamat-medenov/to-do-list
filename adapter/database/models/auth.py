from tokenize import String

from sqlalchemy.orm import Mapped, mapped_column

from adapter.database.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(length=20))
    email: Mapped[int] = mapped_column(String(length=100))


    def __str__(self):
        return self.username
