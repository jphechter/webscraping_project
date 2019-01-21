from django.contrib import admin

from .models import Address, Event, Venue

admin.site.register(Address)
admin.site.register(Event)
admin.site.register(Venue)
