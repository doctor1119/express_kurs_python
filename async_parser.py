import aiohttp
import asyncio
import re
from bs4 import BeautifulSoup


class asyncParser:
    def __init__(self, urls, domain):
        self.urls = urls
        self.domain = domain

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def parsing(self, html, domain):
        data = []
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find_all(class_="tm-article-snippet tm-article-snippet")
        for article in articles:
            author_tag = article.find('a', class_='tm-user-info__userpic')
            author = author_tag.get('title') if author_tag else None
            title = article.find('h2').text
            url = f"{domain}{article.find(class_='tm-title__link').get('href')}"
            date_publication = article.find('time').get('title')
            text = article.find(class_=re.compile(r"article-formatted-body_version-\d+")).text.strip()
            data.append(dict(title=title, author=author, url=url, data=date_publication, summary=text))

        return data

    async def scrape(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            html_contents = await asyncio.gather(*tasks)
            parse_tasks = [self.parsing(html, self.domain) for html in html_contents]
            results = await asyncio.gather(*parse_tasks)

            return results
