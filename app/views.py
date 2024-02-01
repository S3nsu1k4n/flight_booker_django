from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpRequest
from .models import Airport, Flight
from dataclasses import dataclass
from datetime import datetime


class FlightParams:
    '''
    Gets params from search

    Parameters
    ----------
    arrival_airport: int
    departure_airport: int
    passengers: str
    datetime: str
    '''
    def __init__(self, request: HttpRequest) -> None:
        self.arrival_airport: int | None = None
        self.departure_airport: int | None = None
        self.passengers: int | None = None
        self.datetime: str | None = None
        self.chosen_flight: int | None = None
        self._get_params(request=request)
        self._parse_datetime()

    def _get_params(self, request: HttpRequest) -> None:
        '''
        Reads the params from the request

        Parameters
        ----------
        request: HttpRequest
        '''
        for param in self.__dict__.keys():
            self.__dict__[param] = request.GET.get(param)

        self.arrival_airport = int(self.arrival_airport) if self.arrival_airport else None
        self.departure_airport = int(self.departure_airport) if self.departure_airport else None
        self.chosen_flight = int(self.chosen_flight) if self.chosen_flight else None

    def _parse_datetime(self):
        '''
        Parses the datetime from the params

        yyyy-mm-dd --> datetime object
        '''
        if self.datetime != None:
            year, month, day = self.datetime.split('-')
            self.datetime = datetime(year=int(year), month=int(month), day=int(day))


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    params = FlightParams(request=request)

    airports = Airport.objects.all()
    flights = set(map(lambda flight: flight.date_as_string(), Flight.objects.all()))

    available_flights = Flight.objects.filter(arrival_airport=params.arrival_airport, departure_airport=params.departure_airport)

    context = {
        'airports': airports,
        'passengers': range(1, 5),
        'flights': sorted(flights),
        'params': params,
        'available_flights': available_flights,
    }
    if params.chosen_flight == None:
        return render(request, 'index.html', context=context)
    else:
        return redirect(reverse('booking_create') + f'?flight_no={params.chosen_flight}&passengers={params.passengers}')

def booking_create(request: HttpRequest) -> HttpResponse:
    return render(request, 'booking_create.html')