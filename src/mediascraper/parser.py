from argparse import ArgumentParser, RawTextHelpFormatter
from typing import Sequence


class ArgParser:
    """
    Parse console arguments.

    usage: mediascraper.exe [-h] [-u URL] [-s]

    options:
      -h, --help         show this help message and exit
      -u URL, --url URL  URL of the target webpage to scrape
                         This should be a full link, ex. 'https://google.com', not 'google.com'
      -s, --show         Print scraped media links to the console
    """

    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    @classmethod
    def parse_args(cls, args: Sequence[str]) -> dict:
        cls.setup()

        args = cls.parser.parse_args(args)

        return vars(args)

    @classmethod
    def setup(cls):
        cls.parser.add_argument('-u',
                                '--url',
                                type=str,
                                help="URL of the target webpage to scrape\n"
                                "This should be a full link, ex. 'https://google.com', not 'google.com'")

        cls.parser.add_argument('-s',
                                '--show',
                                action='store_true',
                                default=False,
                                help="Print scraped media links to the console")
