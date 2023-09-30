from pydantic import BaseModel, Field


class CreateTodo(BaseModel):
    task: str = Field(max_length=100)
    description: str
    done: bool = False


class UpdateTodo(BaseModel):
    task: str | None = Field(max_length=100)
    description: str | None
    done: bool | None = False
