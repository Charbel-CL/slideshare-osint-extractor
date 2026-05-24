import requests

from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed
)

from app.config import settings
from app.logger import logger


class SlideShareExtractor:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": settings.USER_AGENT
        })

    @retry(
        stop=stop_after_attempt(
            settings.MAX_RETRIES
        ),
        wait=wait_fixed(2),
        reraise=True
    )
    def fetch_search_page(
            self,
            query: str,
            page: int
    ):

        url = (
            f"{settings.BASE_URL}/search/slideshow"
        )

        params = {
            "q": query,
            "page": page
        }

        logger.info(
            f"Fetching page {page} "
            f"for query '{query}'"
        )

        response = self.session.get(
            url,
            params=params,
            timeout=settings.REQUEST_TIMEOUT
        )

        logger.info(
            f"Status code: "
            f"{response.status_code}"
        )

        response.raise_for_status()

        return response.text