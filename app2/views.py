from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def h2(request):
    return HttpResponse('<h1 style="color:green">IT IS THE MOST POWERFULL&FASTEST BIKE IN THE EARTH</h1>')

def buggati(request):
    return HttpResponse('<h1 style="background-color:brown">BUGGATI is one of the most costliest & Hand made car the world</h1>')
