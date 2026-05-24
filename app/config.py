from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    BASE_URL: str = os.getenv(
        "BASE_URL",
        "https://www.slideshare.net"
    )

    REQUEST_TIMEOUT: int = int(
        os.getenv("REQUEST_TIMEOUT", 20)
    )

    MAX_RETRIES: int = int(
        os.getenv("MAX_RETRIES", 3)
    )

    LOG_LEVEL: str = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    USER_AGENT: str = os.getenv(
        "USER_AGENT",
        "Mozilla/5.0"
    )


settings = Settings()