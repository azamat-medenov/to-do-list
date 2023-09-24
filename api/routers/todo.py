from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from sqlalchemy import select

import sys
sys.path.append('..')

from schemas.todo import CreateTodo, UpdateTodo
from adapter.database.db import get_async_session
from adapter.database.models.todo import Todo

todo_router = APIRouter(
    prefix='/api', tags=["Todo"]
)


@todo_router.get('/')
async def get_todos(session: AsyncSession = Depends(get_async_session)):
    query = select(Todo)
    result = await session.execute(query)
    return result.all()


@todo_router.post('/')
async def add_todo(todo: CreateTodo, session: AsyncSession = Depends(get_async_session)):
    return "Not Implemented"


@todo_router.put('/{pk}')
async def update_todo(pk, todo: UpdateTodo, session: AsyncSession = Depends(get_async_session)):
    return "Not Implemented"


@todo_router.delete('/{pk}')
async def delete_todo(pk, session: AsyncSession = Depends(get_async_session)):
    return "Not Implemented"
