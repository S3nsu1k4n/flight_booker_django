from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField('Code', max_length=3, unique=True, help_text='IATA airport code')


class Flight(models.Model):
    start_datetime = models.DateTimeField('Start', help_text='When the flight will start')
    duration = models.DurationField('Duration', help_text='Duration of the flight')
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, help_text='Departure airport', related_name='departing_flights')
    arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, help_text='Arrival airport', related_name='arriving_flights')


class Booking(models.Model):
    pass


class Passenger(models.Model):
    name = models.CharField('Name', max_length=64, help_text='Name of the passenger')
    email = models.EmailField('Email', max_length=64, unique=True, help_text='Email address of the passenger')