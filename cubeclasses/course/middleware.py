from typing import Any
import time

class ExampleMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        execution_time = time.time() - start_time
        print(f"Request execution time: {execution_time:.2f} seconds")
        return response
