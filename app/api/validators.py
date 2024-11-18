from datetime import datetime
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud.rate import rate_crud
from models import Rate


async def check_rate_exists(
        date: datetime,
        cargo_type: str,
        session: AsyncSession,
) -> Rate:
    """
    Проверяет, существует ли тариф для заданной даты и типа груза.
    """
    rate = await rate_crud.get_rate(date, cargo_type, session)
    if not rate:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Тариф не найден"
        )
    return rate


async def check_calculate_value_positive(
        declared_value: float,
) -> None:
    """
    Проверяет, чтобы стоимость была положительной.
    """
    if declared_value <= 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Cтоимость должна быть положительной"
        )
