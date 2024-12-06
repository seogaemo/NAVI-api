import os.path as osp
from pydantic_settings import BaseSettings

envPath = "../../.env"


class Settings(BaseSettings):
    S3_URL: str
    SK_APPKEY: str

    class Config:
        env_file = osp.exists(envPath) and envPath or None
