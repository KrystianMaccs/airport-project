from django.contrib import admin
from .models import Flight

class FlightAdmin(admin.ModelAdmin):
    list_display = ['aeroplane','departure',
                   'arrival_datetime','max_passengers']
    list_filter = ['departure']

    search_fields =['departure']                         # this will add filters and search options in the admin page 

admin.site.register(Flight, FlightAdmin)
