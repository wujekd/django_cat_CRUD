from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import datetime

# Create your views here.

class CatListView(View):
    def get(self, request):
        t = datetime.datetime.now()
        data = {'time' : t}
        return render(request, 'cats/cats_main.html', data)

class CatDetailView(View):
    def get(self, request, pk_from_url):
        return HttpResponse('''<html><body><p>What the fuck lol</p></body></html>''')