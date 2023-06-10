"""Entry point of the program"""

from typing import Sequence

from mediascraper.session import Session
from mediascraper.parser import ArgParser
from mediascraper.scraper import ContentScraper


def main(argv: Sequence[str] | None = None) -> int:
    parser = ArgParser()
    parsed_args: dict = parser.parse_args(argv)

    url: str = parsed_args.get('url')

    if url:
        app_session = Session(url, parsed_args)
        results = app_session.scrape_media(ContentScraper)
        app_session.show_number_of_results(results)
        app_session.apply_flag_args(results)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
