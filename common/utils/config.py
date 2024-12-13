import os.path as osp
from pydantic_settings import BaseSettings

envPath = "../.env"


class Settings(BaseSettings):
    S3_URL: str

    SK_APPKEY: str

    DB_NAME: str = "road"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"

    PREDICTION_URL: str = "http://prediction:9000"

    CORS_ORIGIN: str = ""

    class Config:
        env_file = osp.exists(envPath) and envPath or None
