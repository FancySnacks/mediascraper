"""General utility functions"""

import pathlib

from mediascraper.const import IMAGE_EXTENSIONS, VIDEO_EXTENSIONS, SOUND_EXTENSIONS


def is_image(path: str) -> bool:
    extension = pathlib.Path(path).suffix
    return extension in IMAGE_EXTENSIONS


def is_video(path: str) -> bool:
    extension = pathlib.Path(path).suffix
    return extension in VIDEO_EXTENSIONS


def is_sound(path: str) -> bool:
    extension = pathlib.Path(path).suffix
    return extension in SOUND_EXTENSIONS


def string_list_to_separate_lines(strings: list[str]) -> str:
    return '\n'.join(strings)
