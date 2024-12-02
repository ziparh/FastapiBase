from pydantic_settings import BaseSettings
from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8080

class DataBaseSettings(BaseModel):
    url: str =  "sqlite+aiosqlite:///./api.db"
    echo: bool = True
    echo_pool: bool = True
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DataBaseSettings = DataBaseSettings()

settings = Settings()
