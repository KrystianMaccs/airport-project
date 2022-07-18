from django.contrib import admin
from .models import Flight, Subscription


class FlightAdmin(admin.ModelAdmin):

    search_fields = ['aeroplane','departure__name','destination__name','max_passengers']
    date_hierarchy = 'departure_datetime'
    readonly_fields = ['duration']
    list_filter = ['departure_datetime', 'arrival_datetime']
    list_display= ['aeroplane','departure','destination','departure_datetime',
                'arrival_datetime','duration','max_passengers', 'price']



admin.site.register(Subscription)
admin.site.register(Flight, FlightAdmin)