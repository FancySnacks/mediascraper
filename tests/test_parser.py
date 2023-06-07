import pytest

import pathlib

from mediascraper.parser import ArgParser
from mediascraper.scraper import ContentScraper
from mediascraper.filesaver import FileSaver
from mediascraper.util import is_media

from .util import run_module, Network


def test_args_is_not_none():
    parser = ArgParser()
    args: dict = parser.parse_args(["-s"])
    assert args is not None


def test_args_is_not_none_when_empty():
    parser = ArgParser()
    args: dict = parser.parse_args([])
    assert args is not None


def test_args_raises_exception_when_invalid_args():
    with pytest.raises(SystemExit):
        parser = ArgParser()
        args: dict = parser.parse_args(["-r"])


@pytest.mark.parametrize("args, key", [
    (["-s"], "show")
])
def test_parses_args(args: list[str], key: str):
    parser = ArgParser()
    args: dict = parser.parse_args(args)
    assert args.get(key) is not None


@pytest.mark.skip("TODO: tinker around with 'href' and 'src', otherwise it will always fail")
@Network.requires_connection
def test_parses_filter_arg():
    output = run_module(["-u", "https://google.com", "-f", "all", "-s"]).stdout
    assert all([is_media(link) for link in output])


@Network.requires_connection
def test_parses_show_arg():
    output = run_module(["-u", "https://google.com", "-s"]).stdout
    assert isinstance(output, str)


@Network.requires_connection
def test_parses_txt_save_arg():
    file = "test_parser.txt"
    destination = pathlib.Path.cwd().joinpath(file)
    run_module(["-u", "https://google.com", "--txt", str(destination)])
    assert pathlib.Path.exists(destination) is True
