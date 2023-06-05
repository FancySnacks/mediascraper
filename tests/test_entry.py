import pytest

from mediascraper.__main__ import main

from .util import run_module, Network


def test_run_via_console():
    exit_code = run_module(["-h"]).returncode
    assert exit_code == 0


@Network.requires_connection
def test_entry_point_exit_code_returns_zero_with_args():
    exit_code = main(["-u", "https://google.com"])
    assert exit_code == 0
