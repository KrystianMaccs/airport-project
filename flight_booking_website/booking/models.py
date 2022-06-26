from django.db import models

from flight.models import Flight

class Booking(models.Model):
    reference_no = models.IntegerField()
    passenger_first_name = models.CharField(max_length=20)
    passenger_last_name = models.CharField(max_length=20)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(auto_now_add=True)