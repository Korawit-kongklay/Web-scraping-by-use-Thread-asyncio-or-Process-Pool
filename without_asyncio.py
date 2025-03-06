#web scraping without asyncio
import requests
import time

results = []

def fetch_url(session, url):
    with session.get(url) as response:
        return response.text

def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://x.ai"
    ]
    start_time = time.time()
    
    with requests.Session() as session:
        for i in urls:
            result = fetch_url(session, i)
            results.append(result)

    for i in range(3):
        print(f"{urls[i]}: {len(results[i])} bytes")

    print(f"Time taken: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()