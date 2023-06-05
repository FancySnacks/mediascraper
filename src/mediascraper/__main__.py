import requests

from typing import Sequence

from mediascraper.scraper import ContentScraper
from mediascraper.parser import ArgParser


def main(argv: Sequence[str] | None = None):
    parsed_args: dict = ArgParser.parse_args(argv)

    url: str = parsed_args.get('url')

    if url:
        req = requests.get(url).text
        scraper = ContentScraper.scrape_for_content(req, "img")
        results = ContentScraper.get_tag_attrib(scraper, filter_string="src")

        print(results)


if __name__ == "__main__":
    raise SystemExit(main())
