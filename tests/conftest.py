import pytest

@pytest.fixture
def mock_images() -> list[str]:
    return ["test.png", "test2.jpeg", "test3.svg"]


@pytest.fixture
def mock_html() -> str:
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Test HTML Page</title>
            </head>
        
            <body>
                <img src="/img/test.jpg">
                <img src="/img/test2.png">
            </body>
            </html>
    """
    return html_content
