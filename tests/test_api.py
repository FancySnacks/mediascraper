import pytest

import requests
from requests.exceptions import ConnectionError

from .decorators import Network


# Skip all tests below if there's no internet connection
Network.skip_on_no_connection()


def test_successful_request():
    req = requests.get(url="https://google.com")
    assert req.status_code == 200


def test_unsuccessful_request():
    with pytest.raises(ConnectionError):
        requests.get(url="https://failedrequest.com")
