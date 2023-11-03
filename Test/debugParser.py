import asyncio
from async_parser import asyncParser


async def main(page_count: int):
    urls_to_scrape = [f'{domain}/ru/articles/page{i}/' for i in range(1, page_count + 1)]
    scraper = asyncParser(urls_to_scrape, domain)

    try:
        scrape_results = await scraper.scrape()
        for result in scrape_results:
            print(result)
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")


if __name__ == "__main__":
    page_count = 15
    domain = 'https://habr.com'
    asyncio.run(main(page_count))
