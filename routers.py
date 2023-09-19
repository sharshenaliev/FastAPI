from fastapi import APIRouter, Depends
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from models import User, BankCard
from schemas import BankCardSchema



router = APIRouter(
    prefix="/cards",
    tags=["Operation"]
)


@router.get("/", response_model=list[BankCardSchema])
async def get_list_cards(session: AsyncSession = Depends(get_async_session)):
    query = select(BankCard)
    result = await session.execute(query)
    return result.all()