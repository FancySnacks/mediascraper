import pytest

from typing import Callable

from mediascraper.util import is_video, is_image, is_sound, is_media, MediaType, join_lists
from mediascraper.const import MEDIA_EXTENSIONS


media_extensions: list[list[str]] = list(MEDIA_EXTENSIONS.values())


# Create test cases with parameters
def create_test_cases(extensions: list[str], strategy: Callable) -> list[tuple[str, bool]]:
    params = []
    for ext in extensions:
        case = f"test{ext}"
        params.append((case, strategy(case)))
    return params


IMAGE_CASES = create_test_cases(join_lists(media_extensions), is_image)
VIDEO_CASES = create_test_cases(join_lists(media_extensions), is_video)
SOUND_CASES = create_test_cases(join_lists(media_extensions), is_sound)
ALL_CASES = create_test_cases(join_lists(media_extensions), is_media)


@pytest.mark.parametrize("value, expected", ALL_CASES)
def test_file_is_media(value: str, expected: bool):
    assert is_media(value) is expected


@pytest.mark.parametrize("value, expected", IMAGE_CASES)
def test_file_is_image(value: str, expected: bool):
    assert is_image(value) is expected


@pytest.mark.parametrize("value, expected", VIDEO_CASES)
def test_file_is_video(value: str, expected: bool):
    assert is_video(value) is expected


@pytest.mark.parametrize("value, expected", SOUND_CASES)
def test_file_is_sound(value: str, expected: bool):
    assert is_sound(value) is expected


@pytest.mark.parametrize("value, expected", [
    ("image", MediaType.IMAGE),
    ("video", MediaType.VIDEO),
    ("sound", MediaType.SOUND),
    ("all", MediaType.ALL)
])
def test_str_to_mediatype(value: str, expected: MediaType):
    assert MediaType[value.upper()] is expected
