import logging
import typing as tp

from app.model import Character, CharacterCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

logger = logging.getLogger(__name__)


async def get_all_characters(session: AsyncSession) -> tp.List[Character]:
    result = await session.execute(select(Character))
    return result.scalars().all()


async def get_characters_by_id(
    idx: int, session: AsyncSession
) -> tp.Optional[Character]:
    result = await session.execute(
        select(Character).filter(Character.id == idx)
    )
    res = result.fetchone()

    if res is not None:
        res = res[0]
        if res is not None:
            return Character(
                id=res.id,
                name=res.name,
                has_spouse=res.has_spouse,
                culture=res.culture,
                gender=res.gender,
            )
    return None


async def post_character(
    payload: CharacterCreate, session: AsyncSession
) -> Character:
    character = Character(
        name=payload.name,
        gender=payload.gender,
        has_spouse=payload.has_spouse,
        culture=payload.culture,
    )
    session.add(character)
    await session.commit()
    await session.refresh(character)
    return character
