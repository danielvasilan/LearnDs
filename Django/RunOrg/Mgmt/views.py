from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Event, LocationType, EventLocation

# Event views

class EventListView(ListView):
    model = Event
    ordering = ['-event_date']

class EventDetailView(DetailView):
    model = Event

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'description', 'event_date', 'organizer_id']

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['name', 'description', 'event_date', 'organizer_id']

    # just for having it here
    def test_func(self):
        # event = self.get_object
        if self.request.user == "Admin":
            return True
        return True

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    # just for having it here
    def test_func(self):
        # event = self.get_object
        if self.request.user == "Admin":
            return True
        return True

# LocationType views

class LocationTypeListView(ListView):
    model = LocationType
    ordering = ['name']

class LocationTypeDetailView(DetailView):
    model = LocationType

class LocationTypeCreateView(LoginRequiredMixin, CreateView):
    model = LocationType
    fields = ['name']

# EventLocation views

class EventLocationListView(ListView):
    model = EventLocation
    ordering = ['name']

class EventLocationDetailView(DetailView):
    model = EventLocation

class EventLocationCreateView(LoginRequiredMixin, CreateView):
    model = EventLocation
    fields = ['name', 'description', 'localization', 'location_type']

# other views

def about(request):
    return render(request, 'Mgmt/about.html')
