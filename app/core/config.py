from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Rates'
    database_url: str = "sqlite+aiosqlite:///./smit.db"
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
