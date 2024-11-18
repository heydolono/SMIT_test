import json
from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import Rate
from schemas.rate import RateCreate


async def load_rates_from_json(
        file_content: bytes, session: AsyncSession
) -> str:
    """
    Загрузка тарифов из JSON файла в базу данных.
    """
    try:
        data = json.loads(file_content.decode("utf-8"))
        rates_to_add = []
        for date_str, rates in data.items():
            date = datetime.strptime(date_str, "%Y-%m-%d")
            for rate in rates:
                rate_data = RateCreate(
                    date=date,
                    cargo_type=rate["cargo_type"],
                    rate=rate["rate"]
                )
                rates_to_add.append(
                    Rate(
                        date=rate_data.date,
                        cargo_type=rate_data.cargo_type,
                        rate=rate_data.rate
                    )
                )
        session.add_all(rates_to_add)
        await session.commit()
        return f"Успешно загружено {len(rates_to_add)} тарифов."
    except FileNotFoundError:
        return "Файл не найден. Проверьте путь к файлу."
    except json.JSONDecodeError:
        return "Некорректный формат JSON файла."
    except IntegrityError:
        await session.rollback()
        return "Ошибка загрузки данных: дублирующиеся записи."
    except Exception as e:
        await session.rollback()
        return f"Неизвестная ошибка: {str(e)}"
