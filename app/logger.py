import logging
import colorlog

from app.config import settings


def setup_logger():

    handler = colorlog.StreamHandler()

    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s"
            "[%(asctime)s] "
            "%(levelname)s "
            "%(name)s: "
            "%(message)s"
        )
    )

    logger = logging.getLogger("slideshare_extractor")

    logger.setLevel(settings.LOG_LEVEL)

    logger.addHandler(handler)

    return logger


logger = setup_logger()