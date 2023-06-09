import pytest
import requests

import os
import pathlib

from mediascraper.scraper import ContentScraper
from mediascraper.util import MediaFilter, MediaType, clamp_relative_link

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

    img_to_save = requests.get(content[1]).content

    with open(destination, 'wb') as f:
        f.write(img_to_save)

    assert filename in os.listdir(destination.parent)
    os.remove(destination)


@pytest.mark.skipif(not CONNECTION, reason=Network.skip_reason)
def test_scraped_sound_from_html_is_saved_correctly(path_test):
    filename = 'scrape_save.mp3'
    destination = path_test.joinpath(f'./{filename}')

    url = 'https://wiki.teamfortress.com/wiki/Engineer_responses'
    rq = requests.get(url).text

    scraper = ContentScraper.scrape_for_content(rq, "a")
    content = ContentScraper.get_tag_attrib(scraper, filter_string="href")

    content = MediaFilter(media_type=MediaType.SOUND, items=content).filtered_items

    src = clamp_relative_link(content[5], url)

    sound_to_save = requests.get(src).content

    with open(destination, 'wb') as f:
        f.write(sound_to_save)

    assert filename in os.listdir(destination.parent)
    os.remove(destination)
