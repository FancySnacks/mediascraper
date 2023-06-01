import pytest

from mediascraper.util import is_video, is_image, is_sound
from mediascraper.const import MEDIA_EXTENSIONS


media_extensions = MEDIA_EXTENSIONS.values()


def join_lists(list_of_lists: list[list]):
    a = []
    list_of_lists = list(list_of_lists)
    for item in list_of_lists:
        a.extend(item)
    return a


def create_test_cases(extensions: list[str], strategy) -> list[tuple[str, bool]]:
    params = []
    for ext in extensions:
        case = f"test{ext}"
        params.append((case, strategy(case)))
    return params


IMAGE_CASES = create_test_cases(join_lists(media_extensions), is_image)
VIDEO_CASES = create_test_cases(join_lists(media_extensions), is_video)
SOUND_CASES = create_test_cases(join_lists(media_extensions), is_sound)


@pytest.mark.parametrize("value, expected", IMAGE_CASES)
def test_file_is_image(value: str, expected: bool):
    assert is_image(value) is expected


@pytest.mark.parametrize("value, expected", VIDEO_CASES)
def test_file_is_video(value: str, expected: bool):
    assert is_video(value) is expected


@pytest.mark.parametrize("value, expected", SOUND_CASES)
def test_file_is_sound(value: str, expected: bool):
    assert is_sound(value) is expected
