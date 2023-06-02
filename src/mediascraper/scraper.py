from bs4 import BeautifulSoup


class ContentScraper:

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
        """Return a list of attribute values specified by filter_string parameter"""
        return [item[filter_string] for item in scrape_results]
