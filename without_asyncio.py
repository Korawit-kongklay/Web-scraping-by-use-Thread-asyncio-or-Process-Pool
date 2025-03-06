"""Web scraping without asyncio - sequential URL fetching."""

import requests
import time
from typing import List, Any


def fetch_url(session: requests.Session, url: str) -> str:
    """Fetch content from a URL using requests.

    Args:
        session: requests session object
        url: URL to fetch

    Returns:
        str: Response text content
    """
    with session.get(url) as response:
        return response.text


def main() -> None:
    """Main function to fetch and process URLs sequentially."""
    urls = [
        "https://example.com",
        "https://python.org",
        "https://x.ai",
        "https://youtube.com"

    ]
    results: List[str] = []
    start_time = time.time()

    with requests.Session() as session:
        for url in urls:
            result = fetch_url(session, url)
            results.append(result)

    for url, result in zip(urls, results):
        print(f"{url}: {len(result)} bytes")

    print(f"Time taken: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()