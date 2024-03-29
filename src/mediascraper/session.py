import requests

from typing import  Type

from mediascraper.filesaver import FileSaver
from mediascraper.scraper import ScraperInterface
from mediascraper.util import path_or_url, MediaSourceType, string_list_to_separate_lines, MediaFilter, MediaType, \
    clamp_relative_link, is_direct_url, get_absolute_links


class Session:
    def __init__(self, url: str, args: dict | None = None):
        self.url: str = url
        self.args: dict = args

    def scrape_media(self, scraper: Type[ScraperInterface]) -> list[str]:
        """Scrape media from self.url property, apply filter and return list of urls"""
        if not is_direct_url(self.url):
            req = self.extract_path_or_url(self.url)

            content: list[str] = scraper.scrape_for_content(req, "a")
            results: list[str] = scraper.get_tag_attrib(content, filter_string="href")

            content: list[str] = scraper.scrape_for_content(req, "img")
            results.extend(scraper.get_tag_attrib(content, filter_string="src"))

            results: list[str] = self.apply_media_filter(results)
        else:
            results: list[str] = [self.url]

        return results

    def apply_flag_args(self, results: list[str]):
        """Apply flag parameters from self.args to scraped results"""

        if self.args.get('show') or self.args.get('dir'):
            if self.args.get('verbose'):
                results = get_absolute_links(results, self.url)

            print(string_list_to_separate_lines(results))

        if location := self.args.get('txt'):
            FileSaver.save_links_as_txt(location, results)

        if location := self.args.get('dir'):
            self.download_media(results, location)

    def extract_path_or_url(self, path: str) -> str:
        """
        Returns HTML content of a webpage or html file.

        :param path: path leading to website or system path
        """
        mode = path_or_url(path)

        match mode:
            case MediaSourceType.FILE:
                with open(path) as f:
                    html_content = f.readlines()
                    html_content = string_list_to_separate_lines(html_content)
                return html_content
            case MediaSourceType.URL:
                return requests.get(path).text

    def apply_media_filter(self, results) -> list[str]:
        """
        Apply filter to scraped media

        Do not call this function if you're operating on list that has links directly leading to media
        """

        if media_filter := self.args.get('filter'):
            media_filter = MediaFilter(MediaType[media_filter.upper()], results)
            results = media_filter.filtered_items

        return results

    def download_media(self, results: list[str], path: str):
        """Download and save media to specified directory"""

        self.print_download_start_message()

        for media in results:
            media = clamp_relative_link(media, self.url)
            FileSaver.download_media_from_url(media, path)

    def show_number_of_results(self, results: list[str]):
        """Print all links to scraped media"""
        print(f"Found {len(results)} result(s)")

    def print_download_start_message(self):
        print(f"Downloading media ...")
