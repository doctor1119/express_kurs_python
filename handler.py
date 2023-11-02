class Handler:

    def __init__(self):
        self.data = None

    async def process_request(self, request):
        data = await request.json()
        if data.get('page_count') is None:
            return {"success": False, "error_code": "e01", "message": "page_count is missing or set to None"}
        if not isinstance(data.get('page_count'), int):
            return {"success": False, "error_code": "e02", "message": "page_count is not an int"}
        if data.get('page_count') < 0:
            return {"success": False, "error_code": "e03", "message": "page_count is not a positive number"}

        self.data = data
        return {"success": True, "data": data['page_count']}
