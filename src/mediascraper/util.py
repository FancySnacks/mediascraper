"""General utility functions"""

import pathlib

from typing import Sequence, Callable
from enum import StrEnum, auto

from mediascraper.const import IMAGE_EXTENSIONS, VIDEO_EXTENSIONS, SOUND_EXTENSIONS, MEDIA_EXTENSIONS


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


class MediaType(StrEnum):
    ALL = auto()
    IMAGE = auto()
    VIDEO = auto()
    SOUND = auto()


class MediaFilter:
    """Filter links for specific media type"""

    def __init__(self, media_type: MediaType, items: Sequence):
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
