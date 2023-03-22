import logging
import random
import typing as tp

from app.db import get_session
from app.model import Character, CharacterCreate
from fastapi import Depends, FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud

app = FastAPI()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.get("/ping")
async def get_pong():
    return {"ping": "pong"}


@app.get("/character/{id}", response_model=tp.Optional[Character])
async def get_characters_by_id(
    id: int, session: AsyncSession = Depends(get_session)
):
    result = await crud.get_characters_by_id(id, session)
    return result


@app.get("/character", response_model=tp.List[Character])
async def get_all_characters(session: AsyncSession = Depends(get_session)):
    result = await crud.get_all_characters(session)
    logger.debug(type(result))
    return result


@app.post("/character", response_model=Character)
async def post_character(
    payload: CharacterCreate, session: AsyncSession = Depends(get_session)
):
    if random.randint(0, 1) == 0:
        raise ValueError("err")
    result = await crud.post_character(payload, session)
    return result


Instrumentator().instrument(app).expose(app)
