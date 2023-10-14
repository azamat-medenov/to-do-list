from sqlalchemy import select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.todo import UpdateTodo
from src.adapter.database.models.todo import Todo, UUID_ID


class TodoRepo:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session
        self.model = Todo

    async def update(
            self, user_id: UUID_ID,
            todo_id: UUID_ID, todo: UpdateTodo):
        stmt = (update(self.model)
                .where(self.model.id == todo_id,
                            self.model.user_id == user_id)
                .values(**todo.model_dump())
                .returning(self.model))
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.one()._asdict()

    async def delete(self, user_id: UUID_ID, todo_id: UUID_ID):
        stmt = (delete(self.model)
                .where(self.model.id == todo_id,
                            self.model.user_id == user_id))
        await self.session.execute(stmt)
        await self.session.commit()

    async def create(self, todo: Todo):
        self.session.add(todo)
        await self.session.commit()

    async def get_all(self, user_id: UUID_ID):
        query = await self.session.scalars(
            select(self.model)
            .filter_by(user_id=user_id))
        return query.all()
