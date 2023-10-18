#!/usr/bin/env bash

alembic upgrade head

cd src/api

gunicorn main:main --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000