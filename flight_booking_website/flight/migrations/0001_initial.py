# Generated by Django 4.0.5 on 2022-06-26 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeroplane', models.CharField(max_length=30)),
                ('departure_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Departure Time')),
                ('arrival_datetime', models.DateTimeField(auto_now=True, verbose_name='Arrival Time')),
                ('max_passengers', models.PositiveSmallIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.airport')),
            ],
        ),
    ]
