from pydantic import BaseModel, Field
from datetime import datetime


class CreateTodo(BaseModel):
    task: str = Field(max_length=100)
    done: bool


class UpdateTodo(BaseModel):
    task: str | None = Field(max_length=100)
    done: bool | None
