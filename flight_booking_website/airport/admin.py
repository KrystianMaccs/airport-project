from django.contrib import admin

from .models import Airport

class AirportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Airport, AirportAdmin)
