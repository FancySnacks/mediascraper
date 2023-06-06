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

    def __init__(self):
        self.parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
        self.args = None

    def parse_args(self, args: Sequence[str]) -> dict:
        self.setup()
        self.args: dict = vars(self.parser.parse_args(args))

        return self.args

    def setup(self):
        self.parser.add_argument('-u',
                                 '--url',
                                 type=str,
                                 metavar="webpageURL",
                                 help="URL of the target webpage to scrape\n"
                                      "This should be a full link, ex. 'https://google.com', not 'google.com'")

        self.parser.add_argument('-f',
                                 '--filter',
                                 type=str,
                                 choices=['all', 'image', 'video', 'sound'],
                                 default="all",
                                 metavar="MediaType",
                                 help="Print scraped media links to the console")

        self.parser.add_argument('-s',
                                 '--show',
                                 action='store_true',
                                 default=False,
                                 help="Print scraped media links to the console")

        self.parser.add_argument('--txt',
                                 type=str,
                                 metavar="PATH",
                                 help="Saved scraped links to a text file")
