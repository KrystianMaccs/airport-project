from django.http import HttpResponse
from django.shortcuts import render
from .models import Booking


def home(request):
    contex ={

        'Booking':Booking.objects.filter("Booking_datetime")
    }

    return(request)


def Booking_details(request):    #kind a confused here
    pass


# Create your views here.
