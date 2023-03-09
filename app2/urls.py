from django.urls import path

from app2.views import *

app_name='nothing'

urlpatterns=[
    path('h2/',h2,name='h2'),
    path('buggati/',buggati,name='buggati'),
]