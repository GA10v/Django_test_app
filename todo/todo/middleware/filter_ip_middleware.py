from django.core.exceptions import PermissionDenied
from django.http import response

class FilterIPMiddleweare: # вызываемый класс (класс который можно вызвать, описав его в переменной "MIDDLEWARE"  settings.py)
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        allowed_id = ['127.0.0.1'] # список разрешенных IP Адресов
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_id:
            raise PermissionDenied
        response = self.get_response(request)
        return response