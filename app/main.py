import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core import settings
from api import router as api_router
from core import db_manager


@asynccontextmanager
def lifespan(app: FastAPI):
    # start
    yield
    # shutdown
    db_manager.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.run.host, port=settings.run.port, reload=True)
