#!/usr/bin/env bash


{
    alembic upgrade head
} || {
    sleep 5
    alembic upgrade head
}
uvicorn app.main:app --reload --workers ${APP_NUM_WORKERS} --host 0.0.0.0 --port ${APP_PORT}