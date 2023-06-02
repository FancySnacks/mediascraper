import requests

from mediascraper.scraper import ContentScraper


def main():
    req = requests.get("https://irritant.wordpress.com/").text
    scraper = ContentScraper.scrape_for_content(req, "img")
    results = ContentScraper.get_tag_attrib(scraper, filter_string="src")


if __name__ == "__main__":
    raise SystemExit(main())
