import uuid

from pydantic import BaseModel, Field, ConfigDict



class CreateTodo(BaseModel):
    task: str = Field(max_length=100)
    description: str | None
    done: bool = False


class UpdateTodo(BaseModel):
    task: str | None = Field(max_length=100)
    description: str | None
    done: bool | None = False


class TodoSchema(BaseModel):
    id: uuid.UUID
    task: str
    description: str
    user_id: uuid.UUID
    done: bool

    model_config = ConfigDict(from_attributes=True)

