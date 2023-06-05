import os

from mediascraper.filesaver import FileSaver


def test_file_is_saved_successfully(tmp_path, mock_images):
    filename = "test.txt"
    path = tmp_path.joinpath(filename)
    FileSaver.save_links_as_txt(path, mock_images)

    assert filename in os.listdir(tmp_path)

    with open(path) as f:
        assert len(f.readlines()) > 0
