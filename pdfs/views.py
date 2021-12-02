from django.views.generic.base import View
from django.http import HttpResponse


class HelloWorld(View):
    def get(self, request):
        return HttpResponse(content="Hola mundo cruel")
