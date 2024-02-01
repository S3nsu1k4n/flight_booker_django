from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Airport, Flight
from dataclasses import dataclass


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
    self.arrival_airport = None
    self.departure_airport = None
    self._get_params(request=request)

  def _get_params(self, request: HttpRequest) -> None:
    '''
    Reads the params from the request

    Parameters
    ----------
    request: HttpRequest
    '''
    for param in self.__dict__.keys():
      self.__dict__[param] = request.GET.get(param)

    self.arrival_airport = int(self.arrival_airport)
    self.departure_airport = int(self.departure_airport)


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
  params = FlightParams(request=request)

  airports = Airport.objects.all()
  flights = set(map(lambda flight: flight.date_as_string(), Flight.objects.all()))
  context = {
    'airports': airports,
    'passengers': range(1, 5),
    'flights': flights,
    'params': params,
  }

  return render(request, 'index.html', context=context)
