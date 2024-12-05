from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    S3_URL: str
    SK_APPKEY: str

    model_config = SettingsConfigDict(env_file="../.env")
