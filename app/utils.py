from bs4 import BeautifulSoup  # pip install beautifulsoup4
import aiohttp  # pip install aiohttp
import asyncio
import time


def log_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        all_time = f"{end_time-start_time:.7f}sec 소요"
        return {"result": func(*args, **kwargs), "timer": all_time}

    return wrapper


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        cont_thumb = soup.find_all('div', 'cont_thumb', limit=16)
        for cont in cont_thumb:
            title = cont.find("p", "txt_thumb")
            if title is not None:
                print(title.text)


async def main():
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 3)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
