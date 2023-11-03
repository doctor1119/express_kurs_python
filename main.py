from fastapi import FastAPI, Request, HTTPException
from handler import Handler
from async_parser import asyncParser

app = FastAPI()

domain = 'https://habr.com'


@app.get("/article")
async def get_request(request: Request):
    handler = Handler()
    data = await handler.process_request(request)

    if not data['success']:
        raise HTTPException(status_code=400, detail={"error_code": data["error_code"], "message": data["message"]})

    urls = [f'{domain}/ru/articles/page{i}/' for i in range(1, data['data']['page_count'] + 1)]
    parser = asyncParser(urls, domain)
    scrape_results = await parser.scrape()

    return await handler.process_responce(scrape_results)
