import requests

from typing import Sequence

from mediascraper.scraper import ContentScraper
from mediascraper.parser import ArgParser
from mediascraper.filesaver import FileSaver
from mediascraper.util import string_list_to_separate_lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = ArgParser()
    parsed_args: dict = parser.parse_args(argv)

    url: str = parsed_args.get('url')

    if url:
        req = requests.get(url).text
        scraper = ContentScraper.scrape_for_content(req, "img")
        results = ContentScraper.get_tag_attrib(scraper, filter_string="src")

        if parsed_args.get('show'):
            print(string_list_to_separate_lines(results))

        if location := parsed_args.get('txt'):
            FileSaver.save_links_as_txt(location, results)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
