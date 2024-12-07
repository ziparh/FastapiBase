from pydantic_settings import BaseSettings
from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080

class ApiPrefix(BaseModel):
    api: str = "/api"

class DataBaseSettings(BaseModel):
    url: str =  "sqlite+aiosqlite:///./api.db"
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }



class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: ApiPrefix = ApiPrefix()
    db: DataBaseSettings = DataBaseSettings()

settings = Settings()
