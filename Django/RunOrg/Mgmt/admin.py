from django.contrib import admin
from .models import Event, LocationType, EventLocation, EventRole

admin.site.register(Event)
admin.site.register(EventRole)
admin.site.register(LocationType)
admin.site.register(EventLocation)


