import pytest

import subprocess

from mediascraper.__main__ import main
from mediascraper.const import DEFAULT_PATH

from .decorators import Network


def run_module(args: list[str] = None) -> int:
    path = f"python {DEFAULT_PATH}"

    if args:
        path = path + ' ' + ' '.join(args)

    process = subprocess.run(path, capture_output=True, text=True)

    return process.returncode


def test_run_via_console():
    exit_code = run_module(["-h"])
    assert exit_code == 0


def test_run_via_console_with_correct_args():
    exit_code = run_module(["-h", "https://google.com"])
    assert exit_code == 0


def test_main_function_with_args_returns_zero():
    @Network.requires_connection
    def test_entry_point_exit_code_returns_zero_with_args():
        exit_code = main(["-u", "https://google.com"])
        assert exit_code == 0
