from fastapi import FastAPI, Request, HTTPException
from handler import Handler
from async_parser import asyncParser

app = FastAPI()

urls_to_scrape = ['https://beautiful-soup-4.readthedocs.io/en/latest/']

@app.post("/article")
async def get_request(request: Request):
    handler = Handler()
    data = await handler.process_request(request)

    if data['success'] == False:
        raise HTTPException(status_code=400, detail={"error_code": data["error_code"], "message": data["message"]})

    scraper = asyncParser(urls_to_scrape)
    scrape_results = await scraper.scrape()

    return {
        "data": data,
        "scrape_results": scrape_results
    }
