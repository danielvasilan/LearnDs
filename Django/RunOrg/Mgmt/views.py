from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Event, LocationType, EventLocation, EventArea

from .mygantt import get_gantt

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

    def get_queryset(self):
        self.event_id = get_object_or_404(Event, id=self.kwargs['event_id'])
        return EventLocation.objects.filter(event_id=self.event_id).order_by('shortcode')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add the event_id to the context, for update reasons
        context['event'] = get_object_or_404(Event, id=self.kwargs['event_id'])
        # add the areas 
        context['areas'] = EventArea.objects.all()
        return context


class EventLocationDetailView(DetailView):
    model = EventLocation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gantt'] = get_gantt()
        return context

class EventLocationCreateView(LoginRequiredMixin, CreateView):
    model = EventLocation
    fields = ['shortcode', 'name', 'description', 'location_type', 'area', 'loc_lat', 'loc_lon']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, id=self.kwargs['event_id'])
        return context

    def form_valid(self, form):
        event = get_object_or_404(Event, id=self.kwargs['event_id'])
        form.instance.event_id = event.pk
        return super().form_valid(form)

class EventLocationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EventLocation
    fields = ['shortcode', 'name', 'description', 'location_type', 'area', 'loc_lat', 'loc_lon']

    def test_func(self):
        return True

class EventLocationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EventLocation

    def test_func(self):
        return True

    def get_success_url(self):
        event_id = self.get_object().event.pk
        return reverse('location-list', kwargs={'event_id': event_id})

# other views

def eventGantt(request):
    context = {'gantt_img_path' : get_gantt()}
    return render(request, 'Mgmt/event_gantt.html', context)

def about(request):
    return render(request, 'Mgmt/about.html')
