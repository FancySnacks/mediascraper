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
        """Download image, video or sound file from url to a specified location on the device"""

        filename = pathlib.Path(link).name
        destination = pathlib.Path(save_location).joinpath(filename)

        try:
            content: bytes = requests.get(link).content

            with open(destination, 'wb') as f:
                f.write(content)
        except IOError as e:
            FileSaver._print_invalid_save_location(save_location)
        except requests.exceptions.MissingSchema:
            FileSaver._print_invalid_url(link)
        else:
            FileSaver._print_download_result(link, destination)

    @staticmethod
    def _print_invalid_save_location(loc: str):
        print(f"{loc} is not a valid save location, perhaps try removing the apostrophes / quotation marks?")

    @staticmethod
    def _print_invalid_url(url: str):
        print(f"{url} was not able to be downloaded. Are you sure it's a valid URL?")

    @staticmethod
    def _print_download_result(url: str, path: str | pathlib.Path):
        print(f"{url} was saved to {path}")
