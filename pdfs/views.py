from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render


class HelloWorld(View):
    def get(self, request):
        return HttpResponse(content="Hola mundo cruel")


class HelloWorld2(View):
    def get(self, request):
        data = {
            'name': 'Marco Antonio Albero Albero',
            'years': 39,
            'codes': ['Python', 'Java', 'React']
        }
        return render(request, 'hello_world_template.html', context=data)
