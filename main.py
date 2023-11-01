from fastapi import FastAPI, Request, Response
from hundler import Hundler

app = FastAPI()

@app.post("/article")
async def get_request(request:Request):
    hundler = Hundler()
    data = await hundler.process_request(request)


    return data


