from fastapi import FastAPI

from app.core.logging import setup_loggging
from app.core.database import engine, Base

from contextlib import asynccontextmanager
import logging

# configure logging
setup_loggging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code
    logger.info("Starting up the application...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown code
    logger.info("Shutting down the application...")

app = FastAPI(title="FastAPI Async Postgres Learning", lifespan=lifespan)

@app.get("/")
async def home():
    logger.info("Received request for home endpoint")
    return {
        "message": "Welcome to FastAPI Async Postgres Learning!"
        }
