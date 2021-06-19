import logging
import os

try:
    import coloredlogs
except ImportError:
    coloredlogs = None

FORMAT = (
    "%(asctime)s %(threadName)s %(levelname)s: %(message)s (%(pathname)s:%(lineno)d)"
)

EXCLUDED_LOGGERS = []


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if coloredlogs:
        coloredlogs.install(level="DEBUG", logger=logger)

    for logger_name in EXCLUDED_LOGGERS:
        logger = logging.getLogger(logger_name)
        logger.propagate = False
    logging.debug(f"Logger setup for process {os.getpid()} ....")
