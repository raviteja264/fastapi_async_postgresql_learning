from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import AsyncSessionLocal
from collections.abc import AsyncGenerator
import logging

logger = logging.getLogger(__name__)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    logger.info("Creating new database session")
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            logger.info("Closing database session")
