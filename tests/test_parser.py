import pytest

from mediascraper.parser import ArgParser

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


@Network.requires_connection
def test_parses_show_arg():
    output = run_module(["-u", "https://google.com", "-s"]).stdout
    assert isinstance(output, str)
