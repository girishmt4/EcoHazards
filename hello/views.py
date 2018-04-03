from django.shortcuts import render
from django.http import HttpResponse

from .models import HelloGreeting
from .models import HazardTypes
from .models import HazardReports

import requests


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    hazardreports = HazardReports.objects.all()

    print('in index request')

    #for hazard in hazardreports:
    #   print(hazard.description)
    #  print(hazard.id)
    return render(request, 'index.html', {'hazardReports': hazardreports})
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')


def about(request, extra=None):
    switcher = {
        '-ali': 'about/about-ali.html',
        '-cameron': 'about/about-cameron.html',
        '-girish': 'about/about-girish.html',
        '-humeston': 'about/about-humeston.html',
        '-larsen': 'about/about-larsen.html',
        '-mark': 'about/about-mark.html',
        '-sutherland': 'about/about-sutherland.html'
    }
    if extra:
        return render(request, switcher.get(extra, 'about.html'))
    return render(request, 'about.html')


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def marker(request):
    hazardtypes = HazardTypes.objects.all()

    return render(request, 'marker.html', {'hazardTypes': hazardtypes})


def map(request):
    return render(request, 'map.html')


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
    
def report(request):
    return render(request, 'report.html')


def search(request):
    return render(request, 'search.html')
