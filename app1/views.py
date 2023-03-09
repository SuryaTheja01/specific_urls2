from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Bullet(request):
    return HttpResponse('<h1 style="background-color:green"><marquee>It is the most recelling and trending bike in india</marquee></h1>')

def yamaha(request):
    return HttpResponse('<h1 style="color:blue">it is the best bikes in the world</h1>')
