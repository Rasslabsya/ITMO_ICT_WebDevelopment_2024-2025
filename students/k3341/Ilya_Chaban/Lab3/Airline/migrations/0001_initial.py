# Generated by Django 5.1.4 on 2024-12-25 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('seats', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_airport', models.CharField(max_length=100)),
                ('destination_airport', models.CharField(max_length=100)),
                ('distance', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('seats', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airplanes', to='Airline.airline')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airplanes', to='Airline.aircrafttype')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('education', models.CharField(max_length=255)),
                ('experience', models.PositiveIntegerField()),
                ('passport', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='Airline.airline')),
            ],
        ),
        migrations.CreateModel(
            name='CrewEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_members', to='Airline.crew')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_roles', to='Airline.employee')),
            ],
        ),
        migrations.AddField(
            model_name='crew',
            name='navigator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='navigated_crews', to='Airline.employee'),
        ),
        migrations.AddField(
            model_name='crew',
            name='second_pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_pilot_crews', to='Airline.employee'),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('sold_tickets', models.PositiveIntegerField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='Airline.airplane')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='Airline.route')),
            ],
        ),
        migrations.CreateModel(
            name='FlightInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('actual_departure_time', models.DateTimeField(blank=True, null=True)),
                ('actual_arrival_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('seats_sold', models.PositiveIntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='Airline.flight')),
            ],
        ),
        migrations.CreateModel(
            name='TransitStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_airport', models.CharField(max_length=100)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transit_stops', to='Airline.flight')),
            ],
        ),
    ]
