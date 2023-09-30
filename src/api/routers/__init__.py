from fastapi import FastAPI

from . import auth
from . import todo


def setup(app: FastAPI):
    auth.setup(app)
    todo.setup(app)