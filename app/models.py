from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField('Code', max_length=3, unique=True, help_text='IATA airport code')


class Flight(models.Model):
    start_datetime = models.DateTimeField('Start', help_text='When the flight will start')
    duration = models.DurationField('Duration', help_text='Duration of the flight')
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, help_text='Departure airport', related_name='departing_flights')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, help_text='Arrival airport', related_name='arriving_flights')

    def date_as_string(self) -> str:
        return self.start_datetime.strftime('%Y-%m-%d')


class Passenger(models.Model):
    name = models.CharField('Name', max_length=64, help_text='Name of the passenger')
    email = models.EmailField('Email', max_length=64, unique=True, help_text='Email address of the passenger')

    @classmethod
    def get_by_email(cls, email: str):
        return Passenger.objects.filter(email=email)

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, help_text='The booked flight')
    passengers = models.ManyToManyField(Passenger, related_name='booked_flights')