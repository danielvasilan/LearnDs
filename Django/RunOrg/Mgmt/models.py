from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField (default='<add description here>')
    event_date = models.DateTimeField (default='2020-01-01')

    def __str__(self):
        return self.name

class LocationType(models.Model):
    name = models.CharField (max_length=100)

class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='<add description here>')
    localization = models.TextField(null=True)
    location_type = models.ForeignKey(LocationType, on_delete=models.SET_NULL, null=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

class EventRole(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='<add description here>')

class LocationTask(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default='<add description here>')

