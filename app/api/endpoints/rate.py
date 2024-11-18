from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..validators import (check_rate_exists,
                          check_calculate_value_positive)
from core.db import get_async_session
from schemas.rate import RateDB
from services.rate_loader import load_rates_from_json

router = APIRouter()


@router.post("/load-rate/")
async def load_rate(
        file: UploadFile,
        session: AsyncSession = Depends(get_async_session)):
    """
    Загрузка тарифов из JSON файла.
    """
    if not file.filename.endswith(".json"):
        raise HTTPException(
            status_code=400, detail="Файл должен быть в формате JSON."
        )
    file_content = await file.read()
    result = await load_rates_from_json(file_content, session)
    return {"message": result}


@router.post("/calculate-value/")
async def calculate_value(
        request: RateDB,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Эндпоинт для расчёта стоимости страхования.
    """
    await check_calculate_value_positive(declared_value=request.declared_value)
    rate = await check_rate_exists(
        date=request.date,
        cargo_type=request.cargo_type,
        session=session
    )
    end_cost = request.declared_value * rate.rate
    return {"calculate_value": round(end_cost, 2)}
