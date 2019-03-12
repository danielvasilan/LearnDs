from django.contrib import admin
from .models import Event, LocationType, EventLocation, EventRole, Organizer

admin.site.register(Event)
admin.site.register(EventRole)
admin.site.register(LocationType)
admin.site.register(EventLocation)
admin.site.register(Organizer)


