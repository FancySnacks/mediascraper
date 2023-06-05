import requests

from typing import Sequence

from mediascraper.scraper import ContentScraper
from mediascraper.parser import ArgParser
from mediascraper.util import string_list_to_separate_lines


def main(argv: Sequence[str] | None = None) -> int:
    parsed_args: dict = ArgParser.parse_args(argv)

    url: str = parsed_args.get('url')

    if url:
        req = requests.get(url).text
        scraper = ContentScraper.scrape_for_content(req, "img")
        results = ContentScraper.get_tag_attrib(scraper, filter_string="src")

        if parsed_args.get('show'):
            print(string_list_to_separate_lines(results))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
