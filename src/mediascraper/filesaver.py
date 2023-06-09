"""Handles saving data to files."""

import requests

import pathlib

from mediascraper.util import string_list_to_separate_lines


class FileSaver:
    """Handles saving data to files."""

    @classmethod
    def save_links_as_txt(cls, location, links: list[str]):
        """
        :param location: str - path to save the text file in
        :param links: list[str] - list of media links
        """

        if len(links) == 0:
            raise Exception("Cannot save an empty list!")

        with open(location, "w") as f:
            separated_links = string_list_to_separate_lines(links)
            f.write(separated_links)

    @classmethod
    def download_media_from_url(cls, link: str, save_location: str | pathlib.Path):
        filename = pathlib.Path(link).name
        destination = pathlib.Path(save_location).joinpath(filename)

        content: bytes = requests.get(link).content

        with open(destination, 'wb') as f:
            f.write(content)
