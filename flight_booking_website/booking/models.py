from django.db import models
from Flight.models import Flight
import random


def random_string():
   return str(random.randint(100000, 999999))





## invoking the function

class Booking(models.Model):
    reference_no         = models.CharField(max_length=6, default=random_string, unique=True, editable=False )
    passenger_first_name = models.CharField(max_length=20)
    passenger_last_name  = models.CharField(max_length=20)
    flight               = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_datetime     = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.passenger_first_name
