from django.urls import path 
from . import views

urlpatterns =[
    path('', views.flight_home, name='Home'),
    path('flight_search/', views.flight_search , name='search_result'),
]
