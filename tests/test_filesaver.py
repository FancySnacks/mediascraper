import pytest

import os

from mediascraper.filesaver import FileSaver

from .util import CONNECTION, Network


def test_file_is_saved_successfully(tmp_path, mock_images):
    filename = "test.txt"
    path = tmp_path.joinpath(filename)
    FileSaver.save_links_as_txt(path, mock_images)

    assert filename in os.listdir(tmp_path)

    with open(path) as f:
        assert len(f.readlines()) > 0


def test_raises_exception_when_url_list_is_empty(tmp_path):
    with pytest.raises(Exception):
        FileSaver.save_links_as_txt(tmp_path, [])


@pytest.mark.skipif(not CONNECTION, reason=Network.skip_reason)
def test_media_file_is_downloaded_and_saved_to_device(tmp_path):
    img_url = 'https://www.python.org/static/community_logos/python-logo.png'
    file_name = 'python-logo.png'
    FileSaver.download_media_from_url(img_url, tmp_path)

    assert file_name in os.listdir(tmp_path)
    os.remove(tmp_path.joinpath(f'./{file_name}'))
