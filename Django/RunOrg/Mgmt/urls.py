from django.urls import path
from .views import (
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    LocationTypeListView, LocationTypeDetailView, LocationTypeCreateView,
    EventLocationListView, EventLocationDetailView, EventLocationCreateView, EventLocationUpdateView, EventLocationDeleteView
)
from . import views

urlpatterns = [
    path('', EventListView.as_view(), name='mgmt-home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    path('locationtype/', LocationTypeListView.as_view(), name='locationtype-list'),
    path('locationtype/<int:pk>/', LocationTypeDetailView.as_view(), name='locationtype-detail'),
    path('locationtype/new/', LocationTypeCreateView.as_view(), name='locationtype-create'),

    path('event/<int:event_id>/location/', EventLocationListView.as_view(), name='location-list'),
    path('event/<int:event_id>/location/<int:pk>/', EventLocationDetailView.as_view(), name='location-detail'),
    path('event/<int:event_id>/location/new/', EventLocationCreateView.as_view(), name='location-new'),
    path('event/<int:event_id>/location/<int:pk>/update/', EventLocationUpdateView.as_view(), name='location-update'),
    path('event/<int:event_id>/location/<int:pk>/delete/', EventLocationDeleteView.as_view(), name='location-delete'),

    path('eventgantt/', views.eventGantt, name='event-gantt'),

    path('about/', views.about, name='mgmt-about')
]