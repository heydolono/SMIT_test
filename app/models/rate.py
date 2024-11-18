from sqlalchemy import Column, Date, Float, String

from core.db import Base


class Rate(Base):
    date = Column(Date, nullable=False)
    cargo_type = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
