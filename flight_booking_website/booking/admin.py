from django.contrib import admin

from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display =[ 'reference_no','passenger_first_name', 'passenger_last_name', 'flight' ,'booking_datetime']
    list_filter = ['flight','booking_datetime']
    search_fields = ['reference_no']                # this will add filters and search options in the admin page as mentioned in the excercise3 

admin.site.register(Booking, BookingAdmin)
