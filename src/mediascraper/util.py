"""General utility functions"""

import urllib.parse

import pathlib
import re

from typing import Sequence, Callable
from enum import StrEnum, auto

from mediascraper.const import IMAGE_EXTENSIONS, VIDEO_EXTENSIONS, SOUND_EXTENSIONS, MEDIA_EXTENSIONS


class MediaSourceType(StrEnum):
    """Type of scrape target (webpage url or file path)"""
    URL = auto()
    FILE = auto()


class MediaType(StrEnum):
    """Specifies types of media (all, image, video, sound)"""
    ALL = auto()
    IMAGE = auto()
    VIDEO = auto()
    SOUND = auto()


def is_media(path: str) -> bool:
    extension = pathlib.Path(path).suffix.lower()
    media_extensions = join_lists(list(MEDIA_EXTENSIONS.values()))

    if extension in media_extensions:
        return True
    else:
        return False


def is_image(path: str) -> bool:
    extension = pathlib.Path(path).suffix.lower()
    return extension in IMAGE_EXTENSIONS


def is_video(path: str) -> bool:
    extension = pathlib.Path(path).suffix.lower()
    return extension in VIDEO_EXTENSIONS


def is_sound(path: str) -> bool:
    extension = pathlib.Path(path).suffix.lower()
    return extension in SOUND_EXTENSIONS


def string_list_to_separate_lines(strings: list[str]) -> str:
    return '\n'.join(strings)


# This will join all lists of different media extension types into one shared list
def join_lists(list_of_lists: list[list]) -> list:
    l = []
    for item in list_of_lists:
        l.extend(item)
    return l


def is_scrape_target_a_file(link: str) -> bool:
    is_file: bool = pathlib.Path(link).is_file()
    return is_file


def is_scrape_target_a_html_file(link: str) -> bool:
    if not pathlib.Path(link).suffix == ".html":
        return False

    return True


def is_scrape_target_an_url(link: str) -> bool:
    is_url: re.Match | None = re.fullmatch(r'^https://(\w+)(\.(\w+))*(/*)([\w*/-])*', link)
    return True if is_url else False


def path_or_url(link: str) -> MediaSourceType:
    """Examines whether given link is webpage or a html file"""

    if is_scrape_target_a_file(link):
        if is_scrape_target_a_html_file(link):
            return MediaSourceType.FILE

    return MediaSourceType.URL


def is_direct_url(url: str | pathlib.Path) -> bool:
    """
    Is url leading directly to a file?

    Example:
        'example.com/img_file.png' -> True
        'google.com/stuff' -> False
    """
    is_match = re.search(r'(\b(.)(\w*))$', str(url))
    is_direct = is_match and is_media(url)
    return is_direct


def clamp_relative_link(media_url: str, website_url: str) -> str:
    """Transforms relative link to a fully sized link"""

    link = media_url

    if link.startswith('/') or link.startswith('//'):
        link = urllib.parse.urljoin(website_url, media_url)

    return link


def get_absolute_links(media_links: list[str], website_url: str) -> list[str]:
    return [clamp_relative_link(link, website_url) for link in media_links]


class MediaFilter:
    """
    Filter media links for specific media type

    To access filtered list use 'filtered_items' property

    Parameters:
        media_type: MediaType
            Enum value used for filtering list of media links, each enum is mapped to a filtering function
        items: Sequence[str]
            List of url links / system paths leading to media files

    """

    def __init__(self, media_type: MediaType, items: Sequence[str]):
        self._filter_func: Callable = self._get_media_filter_func(media_type)
        self._filtered_items: list[str] = self._filter(self._filter_func, items)

    def _get_media_filter_func(self, media_type: MediaType) -> Callable:
        match media_type:
            case MediaType.IMAGE: return is_image
            case MediaType.VIDEO: return is_video
            case MediaType.SOUND: return is_sound
            case MediaType.ALL: return is_media
            case _: return is_media

    def _filter(self, filter_func, items) -> list:
        l = []

        for item in items:
            result = filter_func(item)

            if result:
                l.append(item)

        return l

    @property
    def filtered_items(self) -> list[str]:
        return self._filtered_items
