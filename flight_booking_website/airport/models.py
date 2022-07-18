from django.db import models
from django_countries.fields import CountryField


class Airport(models.Model):
    name = models.CharField(max_length=30)
    country = CountryField(blank_label='(select country)')
    airport_code = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        name_list = self.name.split()
        name_code_list = []
        for i in name_list:
            name_code_list.append(i[0])
            self.airport_code  = ''.join(name_code_list)
            self.airport_code 

        super(Airport, self).save(*args, **kwargs)


    class Meta:
        ordering = ["name"]
