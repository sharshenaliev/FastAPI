from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_async_session
from src.models import User


router = APIRouter(
    prefix="/users",
    tags=["Operation"]
)


@router.get("/", response_model=list[User])
async def get_list_cards(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User))
    return result.all()
