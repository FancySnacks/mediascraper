"""Constants"""

import json
import pathlib


def load_media_extensions() -> dict:
    with open(DEFAULT_EXTENSION_LOC, "r") as f:
        extensions = json.load(f)
    return extensions.values()


DEFAULT_PATH = pathlib.Path.cwd()
DEFAULT_EXTENSION_LOC = DEFAULT_PATH.joinpath("./file_extensions.json")

IMAGE_EXTENSIONS, VIDEO_EXTENSIONS, SOUND_EXTENSIONS = load_media_extensions()
