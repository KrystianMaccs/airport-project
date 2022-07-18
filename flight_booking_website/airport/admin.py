from django.contrib import admin

from .models import Airport

class AirportAdmin(admin.ModelAdmin):
    search_fields = ['name','country', 'airport_code']
    list_display = ['name','country', 'airport_code']

admin.site.register(Airport, AirportAdmin)
