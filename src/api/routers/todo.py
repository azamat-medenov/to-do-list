from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, FastAPI

from src.adapter.database.repo.todo import TodoRepo
from src.api.schemas.todo import CreateTodo, UpdateTodo
from src.adapter.database.db import get_async_session
from src.adapter.database.models.auth import User
from src.api.routers.auth import current_user
from src.api.services.todo import TodoService


todo_router = APIRouter(
    prefix='/api/todo', tags=["Todo"]
)


@todo_router.get('')
async def get_todos(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)):
    return await TodoService(TodoRepo, session).get_all(user.id)


@todo_router.post('')
async def create_todo(
        todo: CreateTodo,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)):
    await TodoService(TodoRepo, session).create(user, todo)
    return {'status': 'success'}


@todo_router.put('/{pk}')
async def update_todo(
        pk, todo: UpdateTodo,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)):
    return await (TodoService(TodoRepo, session)
                  .update(user=user, todo_id=pk, todo=todo))


@todo_router.delete('/{pk}')
async def delete_todo(
        pk, session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)):
    await (TodoService(TodoRepo, session)
           .delete(user, pk))
    return 'success delete'


def setup(app: FastAPI):
    app.include_router(todo_router)
