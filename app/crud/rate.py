from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import CRUDBase
from models import Rate


class CRUDRate(CRUDBase):
    async def get_rate(
            self,
            date: datetime,
            cargo_type: str,
            session: AsyncSession,
    ) -> Rate:
        """
        Возвращает тариф по дате и типу груза.
        """
        query = await session.execute(
            select(Rate).where(
                Rate.date == date.date(),
                Rate.cargo_type == cargo_type
        ))
        result = query.scalars().first()
        return result


rate_crud = CRUDRate(Rate)
