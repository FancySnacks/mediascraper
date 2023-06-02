import pytest
import requests


class Network:
    @staticmethod
    def skip_on_no_connection():
        if not CONNECTION:
            pytest.skip(reason="No internet connection", allow_module_level=True)

    @staticmethod
    def connected_to_internet() -> bool:
        try:
            requests.get("https://www.google.com/", timeout=10)
            return True
        except Exception:
            return False


CONNECTION: bool = Network.connected_to_internet()

requires_connection = pytest.mark.skipif(not CONNECTION, reason="No internet connection")
