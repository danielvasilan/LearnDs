from django.db import models
from django.urls import reverse
from PIL import Image

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

class EventLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='<add description here>')
    localization = models.TextField(null=True)
    location_type = models.ForeignKey(LocationType, on_delete=models.PROTECT)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_id.name + ' -> ' + self.name

class EventRole(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='<add description here>')

class LocationTask(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default='<add description here>')

