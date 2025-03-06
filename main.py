#web scraping with asyncio
import asyncio
import aiohttp
import time

tasks = []

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://x.ai"
    ]
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        for i in urls:
            tasks.append(fetch_url(session,i))
        results = await asyncio.gather(*tasks)
    
    for i in range(3):
        print(f"{urls[i]}: {len(results[i])} bytes")

    print(f"Time taken : {time.time() - start_time:.2f} secound")
if __name__ == "__main__":
    asyncio.run(main())