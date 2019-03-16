from django.db import models
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

class Organizer(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    homepage = models.URLField(null=True)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField (default='<add description here>')
    event_date = models.DateTimeField (default='2020-01-01')
    organizer_id = models.ForeignKey(Organizer, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

class LocationType(models.Model):
    name = models.CharField (max_length=100)
    description = models.TextField(default=' ')

    def __str__ (self):
        return self.name

class EventArea(models.Model):
    name = models.CharField(max_length=30)
    shortcode = models.CharField(max_length=5)
    boundaries = models.TextField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.shortcode + ' [' + self.name +']'

class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='<add description here>')
    shortcode = models.CharField(null=True, max_length=10)
    location_type = models.ForeignKey(LocationType, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    area = models.ForeignKey(EventArea, on_delete=models.PROTECT)

    loc_lat = models.FloatField(null=True)
    loc_lon = models.FloatField(null=True)

    def __str__(self):
        return self.event.name + ' -> ' + self.name

    def get_absolute_url(self):
        return reverse('location-list', kwargs={'event_id': self.event.pk})


class EventRole(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='<add description here>')

class TaskStatus(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.code + ' (' + self.description + ')'

class LocationTask(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default='<add description here>')
    taskStart = models.DateTimeField(default=None, blank=True, null=True)
    taskEnd = models.DateTimeField(default=None, blank=True, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    location = models.ForeignKey(EventLocation, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return '[ ' + self.location.name +' ] ' + self.name 

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.PROTECT)



