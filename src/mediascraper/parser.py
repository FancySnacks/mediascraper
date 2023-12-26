from argparse import ArgumentParser, RawTextHelpFormatter
from typing import Sequence


class ArgParser:
    """
    Parse console arguments.

    usage: mediascraper [-h] [-u URL/PATH] [-f MediaType] [-d TargetDir] [-s] [--verbose] [--txt TxtPath] [-v]

    options:
      -h, --help            show this help message and exit
      -u URL/PATH, --url URL/PATH
                            URL of the target webpage to scrape
                            OR system path to html file to scrape
                            In case of links, it should be a full link, ex. 'https://google.com', and not 'google.com'
      -f MediaType, --filter MediaType
                            Print scraped media links to the console
      -d TargetDir, --dir TargetDir
                            Specify directory path to save scraped media in
      -s, --show            Print scraped media links to the console
      --verbose             Print scraped media links as absolute links.
                            Should be used along with '-s' flag.
      --txt TxtPath         Saved scraped links to a text file
      -v, --version         Display current script version
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
                                 metavar="URL/PATH",
                                 help="URL of the target webpage to scrape\n"
                                      "OR system path to html file to scrape\n"
                                      "In case of links, it should be a full link, ex. 'https://google.com', "
                                      "and not 'google.com'")

        self.parser.add_argument('-f',
                                 '--filter',
                                 type=str,
                                 choices=['all', 'image', 'video', 'sound'],
                                 default="all",
                                 metavar="MediaType",
                                 help="Print scraped media links to the console")

        self.parser.add_argument('-d',
                                 '--dir',
                                 type=str,
                                 metavar="TargetDir",
                                 help="Specify directory path to save scraped media in")

        self.parser.add_argument('-s',
                                 '--show',
                                 action='store_true',
                                 default=False,
                                 help="Print scraped media links to the console")

        self.parser.add_argument('--verbose',
                                 action='store_true',
                                 help="Print scraped media links as absolute links.\n"
                                      "Should be used along with '-s' flag.")

        self.parser.add_argument('--txt',
                                 type=str,
                                 metavar="TxtPath",
                                 help="Saved scraped links to a text file")

        self.parser.add_argument('-v',
                                 '--version',
                                 action='store_true',
                                 help="Display current script version")
