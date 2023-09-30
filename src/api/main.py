import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from src.api import routers


def main() -> FastAPI:
    app = FastAPI()
    routers.setup(app)
    return app


def run():
    uvicorn.run('main:main', host='localhost',port=5555)


if __name__ == '__main__':
    run()
