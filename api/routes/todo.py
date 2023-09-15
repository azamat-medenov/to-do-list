from fastapi import APIRouter

from api.schemas.todo import CreateTodo, UpdateTodo

todo_router = APIRouter(
    prefix='/api', tags=["Todo"]
)


@todo_router.get('/')
async def all_todos():
    return "Not Implemented"


@todo_router.post('/')
async def add_todo(todo: CreateTodo):
    return "Not Implemented"


@todo_router.put('/{pk}')
async def update_todo(pk, todo: UpdateTodo):
    return "Not Implemented"


@todo_router.delete('/{pk}')
async def delete_todo(pk):
    return "Not Implemented"
