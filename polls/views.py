from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
import random

class AnkietyBukiety(View):
    def get(self, request):
        return render(request, 'polls/ankiety.html')


def funky(request):
    response = '''<html><body><p>This is the funky function sample</p></body></html>'''
    return HttpResponse(response)

# version vulnerable to cross side scripting
# def danger(request):
#     response = '''<html><body><p>The number is ''' + request.GET['guess'] +'''</p></body></html>'''
#     return HttpResponse(response)

def danger(request, guess):
    response = '''<html><body><p>The number is ''' + guess +'''</p></body></html>'''
    return HttpResponse(response)

def bounce(request):
    return HttpResponseRedirect('https://google.com')

def guess(request):
    f = ['Apple', 'Orange', 'Banana', 'Lychee']
    n = ['Peanuts', 'Cashew']
    context = {'zap' : '42', 'fruits' : f, 'nuts' : n}
    return render(request, 'polls/guess.html', context)

class GameView(View):
    def get(self, request, guess):
        n = random.randint(1,100)
        x = {'guess' : int(guess), 'random' : n }
        return render(request, 'polls/cond.html', x)

