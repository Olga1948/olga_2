import time


class TimeoutMiddleware:
    def __init__(self, get_response, timeout=30):
        self.get_response = get_response
        self.timeout = timeout

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        if end_time - start_time > self.timeout:
            return

        return response
