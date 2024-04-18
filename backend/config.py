import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class DatabaseConfig(BaseModel):
    dsn: str = os.environ.get('DB_URL')


class Config(BaseSettings):
    database: DatabaseConfig = DatabaseConfig()


config = Config()
