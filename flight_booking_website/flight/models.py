from django.db import models
from airport.models import Airport
from django.utils import timezone


class Flight(models.Model):
    aeroplane = models.CharField(max_length=200)
    departure = models.ForeignKey(Airport, related_name='airport_departure', on_delete=models.CASCADE,blank=True, null=True)
    destination = models.ForeignKey(Airport, related_name='airport_destination', on_delete=models.CASCADE, blank=True, null=True)
    departure_datetime = models.DateTimeField(default=timezone.now) 
    arrival_datetime = models.DateTimeField(default=timezone.now)
    max_passengers = models.PositiveIntegerField()
    price = models.PositiveIntegerField()



    
    @property
    def duration(self):
        duration_difference = self.arrival_datetime - self.departure_datetime
        hours = round(duration_difference.total_seconds() / 3600)

        return f"{hours} hours"



    def __str__(self):
        return self.aeroplane
    

    class Meta:
        ordering = ['aeroplane','departure_datetime']


class Subscription(models.Model):
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email