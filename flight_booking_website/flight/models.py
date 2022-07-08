from django.db import models
from airport.models import Airport
from django.utils import timezone


class Flight(models.Model):
    aeroplane = models.CharField(max_length=100)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departure')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination')
    departure_datetime = models.DateTimeField(default=timezone.now)
    arrival_datetime = models.DateTimeField(default=timezone.now)
    max_passengers = models.PositiveIntegerField()
    price = models.PositiveSmallIntegerField()
    

    def __str__(self):
      return self.aeroplane

"""
This decorator calculates the difference 
betwen departure and arrival time
"""
@property
def duration(self):
    duration_difference = self.arrival_datetime - self.departure_datetime
    hours = round(duration_difference.total_seconds() / 3600)
    return f"{hours} hours"