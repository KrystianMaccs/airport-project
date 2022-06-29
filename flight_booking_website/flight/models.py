from django.db import models
from airport.models import Airport
import datetime

class Flight(models.Model):
    aeroplane = models.CharField(max_length=30)
    departure = models.ForeignKey(Airport, null=False, related_name="departure_airport", on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, null=False, related_name="destination_airport", on_delete=models.CASCADE)
    departure_datetime = models.DateTimeField('Departure Time', auto_now_add=True)
    arrival_datetime = models.DateTimeField('Arrival Time', auto_now=True)
    max_passengers = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.aeroplane

    """@property
    def duration(self):
        departure_time = datetime.datetime.now()
        arrival_time = datetime.datetime.now()
        flight_duration = arrival_time - departure_time    #Not sure about this class may be it will work after the tmeplates are added
        return flight_duration"""
