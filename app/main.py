import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core import settings


@asynccontextmanager
def lifispan(api: FastAPI):
    # start
    yield
    # shutdown


app = FastAPI(lifespan=lifispan)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.run.host, port=settings.run.port, reload=True)
