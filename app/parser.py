from bs4 import BeautifulSoup
from datetime import datetime, UTC

from app.models import SlideShareItem
from app.logger import logger


def safe_text(
        element,
        default=None
):

    if not element:
        return default

    return element.get_text(
        strip=True
    )


def safe_int(
        value,
        default=0
):

    try:

        return int(
            str(value)
            .replace(",", "")
            .strip()
        )

    except Exception:

        return default


def parse_search_results(
        html: str,
        page: int
):

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    results = []

    cards = soup.find_all(
        "div",
        class_="search-result"
    )

    logger.info(
        f"Found {len(cards)} result cards"
    )

    for index, card in enumerate(cards):

        try:

            title_element = card.find(
                "a",
                class_="title"
            )

            if not title_element:

                logger.warning(
                    f"Skipping card "
                    f"{index}: missing title"
                )

                continue

            author_element = card.find(
                "span",
                class_="author"
            )

            description_element = card.find(
                "p",
                class_="description"
            )

            views_element = card.find(
                "span",
                class_="views"
            )

            upload_date_element = card.find(
                "span",
                class_="upload-date"
            )

            item = SlideShareItem(
                title=safe_text(
                    title_element,
                    "Unknown Title"
                ),

                url=title_element.get(
                    "href"
                ),

                author=safe_text(
                    author_element
                ),

                description=safe_text(
                    description_element
                ),

                views=safe_int(
                    safe_text(
                        views_element,
                        0
                    )
                ),

                upload_date=safe_text(
                    upload_date_element
                ),

                page=page,

                extracted_at=datetime.now(
                    UTC
                )
            )

            results.append(item)

        except Exception as e:

            logger.error(
                f"Failed parsing card "
                f"{index}: {e}"
            )

    logger.info(
        f"Successfully parsed "
        f"{len(results)} items"
    )

    return results