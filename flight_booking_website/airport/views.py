from django.shortcuts import render
from airport.models import Airport

def airport_home(request):
    return render(request, "airport/airport_home.html")
