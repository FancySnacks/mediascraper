"""Entry point of the program"""

import requests

from typing import Sequence

from mediascraper.scraper import ContentScraper
from mediascraper.parser import ArgParser
from mediascraper.filesaver import FileSaver
from mediascraper.util import string_list_to_separate_lines, MediaFilter, MediaType, \
    MediaSourceType, path_or_url, clamp_relative_link


def show_number_of_results(results: list):
    """Print all links to scraped media"""
    print(f"Found {len(results)} result(s)")


def print_download_start_message():
    print(f"Downloading media ...")


def extract_path_or_url(path: str) -> str:
    """Path parameter is a string system path leading to HTML file OR a string link to a webpage"""
    mode = path_or_url(path)

    match mode:
        case MediaSourceType.FILE:
            with open(path) as f:
                html_content = f.readlines()
                html_content = string_list_to_separate_lines(html_content)
            return html_content
        case MediaSourceType.URL:
            return requests.get(path).text


def main(argv: Sequence[str] | None = None) -> int:
    parser = ArgParser()
    parsed_args: dict = parser.parse_args(argv)

    url: str = parsed_args.get('url')

    if url:
        req = extract_path_or_url(url)

        scraper = ContentScraper.scrape_for_content(req, "a")
        results = ContentScraper.get_tag_attrib(scraper, filter_string="href")

        scraper = ContentScraper.scrape_for_content(req, "img")
        results.extend(ContentScraper.get_tag_attrib(scraper, filter_string="src"))

        if media_filter := parsed_args.get('filter'):
            media_filter = MediaFilter(MediaType[media_filter.upper()], results)
            results = media_filter.filtered_items

        show_number_of_results(results)

        if parsed_args.get('show'):
            print(string_list_to_separate_lines(results))

        if location := parsed_args.get('txt'):
            FileSaver.save_links_as_txt(location, results)

        if location := parsed_args.get('dir'):
            print_download_start_message()

            for media in results:
                media = clamp_relative_link(media, url)
                FileSaver.download_media_from_url(media, location)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
