import logging
import logging.config
import sys

from app.core.config import settings

def setup_loggging() -> None:
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": (
                        "%(asctime)s | "
                        "%(levelname)s | "
                        "%(name)s | "
                        "%(message)s"
                    )
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": sys.stdout,
                    "formatter": "standard"
                }
            },
            "root": {
                "handlers": ["console"],
                "level": settings.LOG_LEVEL
            }
        }
    )