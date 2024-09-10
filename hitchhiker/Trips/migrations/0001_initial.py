# Generated by Django 4.2.16 on 2024-09-09 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_Date', models.DateField()),
                ('depart_Time', models.TimeField()),
                ('FreeWeight', models.FloatField()),
                ('ComsumedWeight', models.FloatField(default='0.00')),
                ('TotalWeightTrip', models.FloatField(default='0.00')),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_from_location', to='locations.locationmodel')),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_to_location', to='locations.locationmodel')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
