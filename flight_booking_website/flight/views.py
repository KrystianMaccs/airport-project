from django.shortcuts import render
#from flight.models import Flight
from django.http import HttpResponseRedirect

from .forms import FlightForm

def flight_home(request):
    return render(request, 'flight/flight_home.html')


def flight_search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FlightForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FlightForm()

    return render(request, 'flight_search.html', {'form': form})

