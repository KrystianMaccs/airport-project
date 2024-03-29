# Generated by Django 4.0.5 on 2022-07-18 10:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_subscription_alter_flight_options_and_more'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['flight__departure_datetime']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='passenger_first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='passenger_last_name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_flight', to='flight.flight'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='reference_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='passengers',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='booking.passenger'),
        ),
    ]
