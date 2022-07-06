from unicodedata import name
from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=15)
    airport_code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


    class Meta:
        order_by = ["name"]
