# analytics/middleware.py
from .models import APIRequest

class APIRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.path.startswith('/api/') and request.user.is_authenticated:
            APIRequest.objects.create(
                user=request.user,
                endpoint=request.path,
                method=request.method
            )
        
        return response