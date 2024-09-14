from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    title: str = 'Приложение QRKot'
    description: str = 'Описание приложения QRKot'
    database_url: str
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
