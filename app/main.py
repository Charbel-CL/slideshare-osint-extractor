import argparse
import json

from app.logger import logger
from app.extractor import SlideShareExtractor
from app.parser import parse_search_results


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--query",
        required=True,
        help="Search keyword"
    )

    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Maximum pages to retrieve"
    )

    parser.add_argument(
        "--fixture",
        action="store_true",
        help="Use local fixture HTML"
    )

    parser.add_argument(
        "--output",
        default="output/results.json",
        help="Output JSON path"
    )

    args = parser.parse_args()

    extractor = SlideShareExtractor()

    all_results = []

    for page in range(1, args.pages + 1):

        try:

            if args.fixture:

                logger.info(
                    f"Loading fixture page {page}"
                )

                with open(
                        "fixtures/sample_search.html",
                        "r",
                        encoding="utf-8"
                ) as file:

                    html = file.read()

            else:

                html = extractor.fetch_search_page(
                    query=args.query,
                    page=page
                )

            results = parse_search_results(
                html=html,
                page=page
            )

            all_results.extend(results)

        except Exception as e:

            logger.error(
                f"Failed processing "
                f"page {page}: {e}"
            )

    unique_results = {
        item.url: item
        for item in all_results
    }

    final_results = list(
        unique_results.values()
    )

    logger.info(
        f"Total unique results: "
        f"{len(final_results)}"
    )

    with open(
            args.output,
            "w",
            encoding="utf-8"
    ) as file:

        json.dump(
            [
                item.model_dump(
                    mode="json"
                )
                for item in final_results
            ],
            file,
            indent=4,
            ensure_ascii=False
        )

    logger.info(
        f"Results exported to "
        f"{args.output}"
    )


if __name__ == "__main__":
    main()