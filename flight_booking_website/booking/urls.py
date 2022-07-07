from django import views
from django.urls import path 
from .models import Booking


urlpatterns =[

    path('',views.home, name='home')
]
