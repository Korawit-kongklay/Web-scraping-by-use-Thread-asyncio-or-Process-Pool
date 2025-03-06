"""Web scraping with asyncio to fetch content from multiple URLs concurrently."""

import asyncio
import aiohttp
import time
from typing import List


async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    """Fetch content from a URL asynchronously.

    Args:
        session: aiohttp client session
        url: URL to fetch

    Returns:
        str: Response text content
    """
    async with session.get(url) as response:
        return await response.text()


async def main() -> None:
    """Main async function to fetch and process URLs."""
    urls = [
        "https://example.com",
        "https://python.org",
        "https://x.ai",
        "https://youtube.com"
    ]
    tasks = []
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_url(session, url))
        results = await asyncio.gather(*tasks)

    for url, result in zip(urls, results):
        print(f"{url}: {len(result)} bytes")

    print(f"Time taken: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())