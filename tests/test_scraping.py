import requests

from mediascraper.scraper import ContentScraper
from mediascraper.util import is_image

from .util import Network


def test_successful_scrape_images_with_mock_html_page(mock_html):
    content = ContentScraper.scrape_for_content(mock_html)
    assert isinstance(content, list)


def test_scrape_for_images_only(mock_html):
    content = ContentScraper.scrape_for_content(mock_html, "img")
    images: list[str] = ContentScraper.get_tag_attrib(content, "src")
    assert all([is_image(img) for img in images])


@Network.requires_connection
def test_scrape_a_website_for_images():
    html = requests.get("https://twitter.com/home").text
    content = ContentScraper.scrape_for_content(html, "img")
    images = ContentScraper.get_tag_attrib(content, "src")
    assert all([is_image(img) for img in images])
