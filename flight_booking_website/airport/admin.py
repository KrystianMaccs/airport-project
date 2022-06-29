from django.contrib import admin

from .models import Airport

class AirportAdmin(admin.ModelAdmin):
    list_display = ['name','country','code']  #This will add the filters in the admin page
    list_filter = ['name','country','code']   
    search_fields = ['country']               # We can search by this in the admin page

admin.site.register(Airport, AirportAdmin)
