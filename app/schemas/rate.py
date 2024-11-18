from datetime import datetime

from pydantic import BaseModel, Field, condecimal, root_validator


class RateBase(BaseModel):
    date: datetime
    cargo_type: str = Field(..., min_length=1, max_length=50)

    @root_validator(pre=True)
    def validate_date_format(cls, values):
        date_str = values.get('date')
        if isinstance(date_str, str):
            try:
                values['date'] = datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Должен быть 'YYYY-MM-DD' формат")
        return values
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d')
        }
        schema_extra = {
            "example": {
                "date": "2020-06-01",
                "cargo_type": "Glass",
                "declared_value": 1000
            }
        }


class RateCreate(RateBase):
    rate: condecimal(gt=0, decimal_places=5)


class RateDB(RateBase):
    declared_value: float
