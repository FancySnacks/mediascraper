import pytest

import pathlib


PATH = pathlib.Path(__file__).parent


@pytest.fixture
def path_test():
    return PATH


@pytest.fixture
def mock_images() -> list[str]:
    return ["test.png", "test2.jpeg", "test3.svg"]


@pytest.fixture
def mock_html() -> str:
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Test HTML Page</title>
            </head>
        
            <body>
                <img src="{PATH.joinpath('./img/test.jpg')}">
                <img src="{PATH.joinpath('./img/python-logo.png')}">
            </body>
        </html>
    """
    return html_content
