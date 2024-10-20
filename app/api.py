import requests
import asyncio

async def fetch(url):
    # Use asyncio.to_thread to run the blocking requests.get in a non-blocking way
    response = await asyncio.to_thread(requests.get, url)
    
    if response.status_code == 200:
        return response.json()  # Return JSON data if the request is successful
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

async def main():
    urls = [
        'https://stoic.tekloon.net/stoic-quote'
    ]
    
    tasks = [fetch(url) for url in urls]  # Create a list of fetch tasks
    results = await asyncio.gather(*tasks)  # Run all tasks concurrently

    for result in results:
        if result:
            print(result)  # Print the fetched data

# Run the main coroutine
asyncio.run(main())
