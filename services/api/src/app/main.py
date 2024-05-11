from fastapi import FastAPI
from app.exceptions import generic_exception_handler
from app.routes import router
from contextlib import asynccontextmanager
from src.logging.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

setup_logging()

app = FastAPI(lifespan=lifespan)
app.include_router(router)

# Handler for unhandled exceptions, it will log them to logs/app.log
app.add_exception_handler(Exception, generic_exception_handler)
