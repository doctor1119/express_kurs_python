import aiohttp
import asyncio
from bs4 import BeautifulSoup


class asyncParser:
    def __init__(self, urls):
        self.urls = urls

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        return [link.get('href') for link in links]

    async def scrape(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            html_contents = await asyncio.gather(*tasks)

            parse_tasks = [self.parse(html) for html in html_contents]
            results = await asyncio.gather(*parse_tasks)

            return results

