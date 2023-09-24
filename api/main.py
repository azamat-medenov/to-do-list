from fastapi import FastAPI

from routers.todo import todo_router

app = FastAPI()

app.include_router(todo_router)

