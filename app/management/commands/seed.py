from django.core.management.base import BaseCommand
from ...models import Airport, Flight
import random
from datetime import datetime, timedelta, timezone
import time


def get_random_letters(n=1, *args: tuple) -> str:
    if len(args) == 0 or not isinstance(args[0], str):
        return get_random_letters(n, '')
    
    if n > 0:
        return get_random_letters(n-1, args[0] + chr(random.randrange(ord('A'), ord('Z'))))
    else:
        return args[0]


class Command(BaseCommand):
    help = 'seed database for development'

    def handle(self, *args, **options):
        #executes seed command
        self.stdout.write('Deleting data...')
        self.delete_all()
        self.stdout.write('Done')
        self.stdout.write('Seeding data...')
        self.seed()
        self.stdout.write('Done')

    def delete_all(self):
        Airport.objects.all().delete()
        Flight.objects.all().delete()

    def seed(self):
        self.seed_airports()
        self.seed_flights()

    def seed_airports(self):
        t1 = time.perf_counter()
        for i in range(10):
            a = Airport(code=get_random_letters(3))
            a.save()
        
        self.stdout.write(f'Added {len(Airport.objects.all())} airports [{time.perf_counter() - t1}]')

    def seed_flights(self):
        t1 = time.perf_counter()
        airports = Airport.objects.all()
        for i in range(10):
            departure = random.choice(airports)
            arrival = random.choice(airports)

            while departure == arrival:
                arrival = random.choice(airports)

            f = Flight(start_datetime=datetime.now(tz=timezone.utc) + timedelta(days=random.randint(0, 61)),
                       duration=timedelta(hours=random.randint(1, 20)),
                       departure=departure,
                       arrival=arrival,
                       )
            f.save()

        self.stdout.write(f'Added {len(Flight.objects.all())} flights [{time.perf_counter() - t1}]')