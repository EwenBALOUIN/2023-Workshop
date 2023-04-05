from django.shortcuts import redirect
from django.urls import reverse

class BlockBackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 302 and response.url == reverse('logout'):
            request.session['block_back'] = True
        elif request.session.get('block_back', False):
            request.session['block_back'] = False
            return redirect(reverse('login'))
        return response
