from argparse import ArgumentParser
from typing import Sequence


class ArgParser:
    parser = ArgumentParser()

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
                                help="URL of the target webpage to scrape")
