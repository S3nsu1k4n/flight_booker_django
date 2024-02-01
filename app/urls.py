from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('flights/', view=views.index, name='flights_index'),
    path('booking/new', view=views.booking_new, name='booking_new'),
    path('booking/create', view=views.booking_create, name='booking_create'),
]