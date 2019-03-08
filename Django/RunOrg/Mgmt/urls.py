from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mgmt-home'),
    path('about/', views.about, name='mgmt-about')
]