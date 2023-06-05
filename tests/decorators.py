import pytest
import requests


class Network:
    skip_reason = "No internet connection"

    @staticmethod
    def skip_on_no_connection():
        if not CONNECTION:
            pytest.skip(reason=Network.skip_reason, allow_module_level=True)

    @staticmethod
    def connected_to_internet() -> bool:
        try:
            requests.get("https://www.google.com/", timeout=10)
            return True
        except Exception as e:
            return False

    @staticmethod
    def requires_connection(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        if CONNECTION is False:
            pytest.mark.skip(reason=Network.skip_reason)

        else:
            return wrapper



CONNECTION: bool = Network.connected_to_internet()
