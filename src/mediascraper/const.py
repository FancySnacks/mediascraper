"""Constants"""

import json
import pathlib

from enum import StrEnum, auto


class MediaType(StrEnum):
    IMAGE = auto()
    VIDEO = auto()
    SOUND = auto()


def load_media_extensions_from_file() -> dict:
    with open(DEFAULT_EXTENSION_LOC, "r") as f:
        extensions: dict = json.load(f)
    return extensions


DEFAULT_PATH = pathlib.Path(__file__).parent
DEFAULT_EXTENSION_LOC = DEFAULT_PATH.joinpath("./file_extensions.json")

MEDIA_EXTENSIONS: dict = load_media_extensions_from_file()

IMAGE_EXTENSIONS = MEDIA_EXTENSIONS['image']
VIDEO_EXTENSIONS = MEDIA_EXTENSIONS['video']
SOUND_EXTENSIONS = MEDIA_EXTENSIONS['sound']
