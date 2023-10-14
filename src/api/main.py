import uvicorn
from fastapi import FastAPI
from src.api import routers


def main() -> FastAPI:
    app = FastAPI()
    routers.setup(app)
    return app


def run():
    uvicorn.run(app='main:main', host='localhost', port=8000, reload=True)


if __name__ == '__main__':
    run()
