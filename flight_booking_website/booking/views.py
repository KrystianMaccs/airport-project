from multiprocessing import context
from django.shortcuts import render
from .models import Booking


def booking_home(request):
    context ={

        "Booking": Booking.objects.filter("Booking_datetime")
    }

    return render(request, 'booking/booking_home.html', context)


def Booking_details(request):    #kind a confused here
    pass

