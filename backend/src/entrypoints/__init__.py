import logging
import os

from typing import List

try:
    import coloredlogs
except ImportError:
    coloredlogs = None

FORMAT: str = (
    "%(asctime)s %(threadName)s %(levelname)s: %(message)s (%(pathname)s:%(lineno)d)"
)

EXCLUDED_LOGGERS: List[str] = []


def init_logging() -> None:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if coloredlogs:
        coloredlogs.install(level="DEBUG", logger=logger)

    for logger_name in EXCLUDED_LOGGERS:
        logger = logging.getLogger(logger_name)
        logger.propagate = False
    logging.debug(f"Logger setup for process {os.getpid()} ....")
