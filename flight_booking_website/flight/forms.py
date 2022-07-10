from django import forms

class FlightForm(forms.Form):
    departure_destination = forms.CharField(label='Departure Destination', max_length=80)
    departure_date = forms.CharField(label='Departure date')
    destination_date = forms.CharField(label='Destination Date')