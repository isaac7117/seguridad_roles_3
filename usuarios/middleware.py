from django.shortcuts import redirect
from django.urls import reverse

class RolMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith('/usuarios/login/'):
            return redirect(reverse('login'))

        if request.path.startswith('/admin') and request.user.rol != 'admin':
            return redirect(reverse('inicio'))

        response = self.get_response(request)
        return response