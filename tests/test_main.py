from mediascraper.__main__ import main
from mediascraper.parser import ArgParser


@classmethod
def mock_arg_setup(cls):
    cls.parser.add_argument('-t',
                            '--test',
                            action='store_true',
                            help="Test argument, do not use.\n")


ArgParser.setup = mock_arg_setup


def test_entry_point_exit_code_returns_zero():
    exit_code = main(["-t"])
    assert exit_code == 0
