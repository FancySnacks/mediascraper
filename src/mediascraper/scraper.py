"""Extract elements from HTML page"""
from bs4 import BeautifulSoup

from typing import Protocol


class ScraperInterface(Protocol):
    """ContentScraper protocol class"""

    @classmethod
    def scrape_for_content(cls, html_content: str, tag: str = None, attrs: dict = None) -> list:
        """
            Scrape through html file for results matching the tag parameter

            :param html_content: str - HTML markdown content as a string
            :param tag: str - only search for elements that match this HTML tag
            :param attrs: dict - additional filters for tag attributes

            Returns list of matching HTML tags
        """
        pass

    @classmethod
    def get_tag_attrib(cls, scrape_results: list, filter_string: str) -> list[str]:
        """
        Return a list of attribute values specified by filter_string parameter

        Parameters:
            scrape_results: list - list of scraped HTML content as provided by scrape_for_content() function
            filter_string: str - html attribute to extract value from, usually 'href' or 'src'
        """
        pass

    @classmethod
    def _tag_exists(cls, item, filter_string: str):
        """Check if specified HTML tag exists (filter_string param) for this HTML tag (item)"""
        pass


class ContentScraper:
    """
    Scrapes through html file or webpage in search for media files.

    use scrape_for_contents() function for scraping
    """

    @classmethod
    def scrape_for_content(cls, html_content: str, tag: str = None, attrs: dict = None) -> list:
        """
        Scrape through html file for results matching the tag parameter

        :param html_content: str - HTML markdown content as a string
        :param tag: str - only search for elements that match this HTML tag
        :param attrs: dict - additional filters for tag attributes

        Returns list of matching HTML tags
        """
        soup = BeautifulSoup(html_content, "html.parser")
        results = soup.find_all(tag, attrs=attrs)

        return results

    @classmethod
    def get_tag_attrib(cls, scrape_results: list, filter_string: str) -> list[str]:
        """
        Return a list of attribute values specified by filter_string parameter

        Parameters:
            scrape_results: list - list of scraped HTML content as provided by scrape_for_content() function
            filter_string: str - html attribute to extract value from, usually 'href' or 'src'
        """

        scrape_results = list(set(scrape_results))

        filtered_results = [item for item in scrape_results if ContentScraper._tag_exists(item, filter_string)]

        return [item[filter_string] for item in filtered_results]

    @classmethod
    def _tag_exists(cls, item, filter_string: str) -> bool:
        """Check if specified HTML tag exists (filter_string param) for this HTML tag (item)"""
        if item.get(filter_string):
            return True
        else:
            return False
