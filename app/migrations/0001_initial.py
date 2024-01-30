# Generated by Django 5.0 on 2024-01-30 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='IATA airport code', max_length=3, unique=True, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the passenger', max_length=64, verbose_name='Name')),
                ('email', models.EmailField(help_text='Email address of the passenger', max_length=64, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(help_text='When the flight will start', verbose_name='Start')),
                ('duration', models.DurationField(help_text='Duration of the flight', verbose_name='Duration')),
                ('arrival', models.ForeignKey(help_text='Arrival airport', on_delete=django.db.models.deletion.CASCADE, related_name='arriving_flight', to='app.airport')),
                ('departure', models.ForeignKey(help_text='Departure airport', on_delete=django.db.models.deletion.CASCADE, related_name='departing_flight', to='app.airport')),
            ],
        ),
    ]