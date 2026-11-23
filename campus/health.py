# campus/health.py
from django.db import connection
from django.http import HttpResponse

class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health/":
            try:
                with connection.cursor() as c:
                    c.execute("SELECT 1")
            except Exception:
                return HttpResponse("page is unavailable", status=503)
            return HttpResponse("ok", status=200)
        return self.get_response(request)