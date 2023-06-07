import pytest
import requests

import pathlib

from mediascraper.scraper import ContentScraper
from mediascraper.util import is_image, is_scrape_target_a_file, is_scrape_target_an_url
from mediascraper.const import DEFAULT_PATH

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


@pytest.mark.parametrize('url, expected', [
    ('https://regex101.com/', True),
    ('https://regex101.com', True),
    ('https://regex101.com', True),
    ('https://irritant.wordpress.com/2023/03/30/big-bug-fix-and-more-artistic-updates/', True),
    ('https://test.com/test-test/test', True),
    ('//site.com/', False),
    ('site.com', False),
    ('site.site.com', False),
    ('site.com/test/', False),
])
def test_scrape_source_is_valid_url(url, expected):
    assert is_scrape_target_an_url(url) is expected


@pytest.mark.parametrize('path, expected', [
    (str(DEFAULT_PATH.joinpath('const.py')), True),
    ('.', False),
    ('', False),
])
def test_scrape_source_is_valid_path(path, expected):
    assert is_scrape_target_a_file(path) is expected
