from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.database.repo.todo import TodoRepo
from src.api.schemas.todo import CreateTodo, UpdateTodo
from src.adapter.database.models.todo import UUID_ID
from src.adapter.database.models.auth import User


class TodoService:
    def __init__(
            self, repo: Type[TodoRepo],
            session: AsyncSession):
        self.repo = repo(session)

    async def create(
            self, user: User,
            todo: CreateTodo):
        new_todo = self.repo.model(
            **todo.model_dump(),
            user_id=user.id,
            user=user)
        await self.repo.create(new_todo)

    async def update(
            self, user: User, todo_id: UUID_ID,
            todo: UpdateTodo):
        return await self.repo.update(
            user_id=user.id,
            todo_id=todo_id,
            todo=todo)

    async def delete(self, user: User, todo_id: UUID_ID):
        return await self.repo.delete(user.id, todo_id)

    async def get_all(
            self, user_id: UUID_ID):
        return [row.read_model().model_dump()
                for row in await self.repo.get_all(user_id)]
