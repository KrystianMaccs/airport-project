from django.contrib import admin
from .models import Flight

class FlightAdmin(admin.ModelAdmin):
    list_display = ['aeroplane','departure',
                   'arrival_time','max_passengers']
    list_filter = ['aeroplane','destination','arrival_time','max_passengers',]

    search_fields =['departure']                         # this will add filters and search options in the admin page 

admin.site.register(Flight, FlightAdmin)
