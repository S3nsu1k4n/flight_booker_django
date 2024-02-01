from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Airport, Flight

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
  airports = Airport.objects.all()
  flights = set(map(lambda flight: flight.date_as_string(), Flight.objects.all()))
  context = {
    'airports': airports,
    'passengers': range(1, 5),
    'flights': flights,
  }

  return render(request, 'index.html', context=context)
