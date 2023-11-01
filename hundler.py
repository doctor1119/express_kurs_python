from fastapi import HTTPException

class Hundler:

    async def process_request(self, request):
        data = await request.json()
        if data.get('page_count') is None:
            raise HTTPException(status_code=400, detail="page_count is missing or set to None")
        if not isinstance(data.get('page_count'), int):
            raise HTTPException(status_code=400, detail="page_count is not int")
        if data.get('page_count') < 0:
            raise HTTPException(status_code=400, detail="page_count is not positive number")
        return data

