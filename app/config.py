#centralizar toda nossa configuração

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGODB_URI: str
    DB_NAME: str = 'aula_nosql'

    #configurar o pydantic para ler o arquivo .env

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_prefixe = "",
        extra = "ignore"
    )
settings = Settings()