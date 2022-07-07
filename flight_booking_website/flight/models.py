from django.db import models
from Airport.models import Airport
from datetime import datetime



def difference(h1, m1,h2, m2):

  t1 =h1 *60 +m1  
  t2 = h2 * 60 + m2



class Flight(models.Model):

    aeroplane = models.CharField(max_length=100)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departure')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination')
    departure_datetime = models.DateTimeField(auto_now_add=True)
    arrival_datetime = models.DateTimeField( max_length=100)  # have to add manually on the database and before doing that make migrations
    max_passengers = models.PositiveIntegerField()
    price = models.PositiveSmallIntegerField()
    


    def __str__(self):
      return self.aeroplane



    
    @property
    def hourdiff(self):


      t1 = h1 * 60 + m1
      t2 = h2 * 60 + m2

      h1 = self.arrival_datetime.hour
      m1 = self.arrival_datetime.minute
      h2 = self.departure_datetime.hour
      m2 = self.departure_datetime.minute

      if (t1==t2):
        print("Both are same time")
      else:
        diff = t2 - t1
   
      h = (int(diff/60)) % 24
      m = diff % 60


      return f"{diff}  hours"

    def __str__(self):
       return str(self.departure)+ "" + "to" +str(self.destination) 
