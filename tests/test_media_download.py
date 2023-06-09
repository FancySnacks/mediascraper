import pytest
import requests

import os
import pathlib

from mediascraper.scraper import ContentScraper

from .util import CONNECTION, Network


def test_scraped_image_is_saved_correctly(mock_html: str, path_test):
    filename = 'save_test.jpg'
    destination = pathlib.Path(path_test).joinpath(filename)

    with open(path_test.joinpath('./img/python-logo.png'), 'rb') as f:
        content = f.read()

    with open(destination, 'wb') as f:
        f.write(content)

    assert filename in os.listdir(destination.parent)
    os.remove(destination)


@pytest.mark.skipif(not CONNECTION, reason=Network.skip_reason)
def test_scraped_image_from_html_is_saved_correctly(path_test):
    filename = 'scrape_save.jpg'
    destination = path_test.joinpath(f'./{filename}')

    rq = requests.get('https://www.teamfortress.com/')

    scraper = ContentScraper.scrape_for_content(rq.text, "img")
    content = ContentScraper.get_tag_attrib(scraper, filter_string="src")
    print(content)

    img_to_save = requests.get(content[1]).content

    with open(destination, 'wb') as f:
        f.write(img_to_save)

    assert filename in os.listdir(destination.parent)
    os.remove(destination)
