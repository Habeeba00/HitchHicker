from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class locationModel(models.Model):
    CITY_CHOICES = (
        ('london', 'London'),
        ('paris', 'Paris'),
        ('Sydney', 'Sydney'),
        ('Tokyo', 'Tokyo'),
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Hong_Kong', 'Hong Kong'),
        ('Berlin', 'Berlin'),
        ('Madrid', 'Madrid'),
        ('Rome', 'Rome'),
        ('Barcelona', 'Barcelona'),
        ('Moscow', 'Moscow'),
        ('Athens', 'Athens'),
        ('Istanbul', 'Istanbul'),
        ('Los_Angeles', 'Los Angeles'),
        ('Miami', 'Miami'),
        ('San_Francisco', 'San Francisco'),
        ('Mexico', 'Mexico'),
        ('Cairo', 'Cairo'),
        ('Algiers', 'Algiers'),
        ('Berlin', 'Berlin'),
        ('Vienna', 'Vienna'),
        ('Amsterdam', 'Amsterdam'),
        ('Berlin', 'Berlin'),
        ('Alexandria', 'Alexandria'),
        ('Tunis', 'Tunis'),
        ('Riyadh', 'Riyadh'),
        ('Jeddah', 'Jeddah'),
        ('Giza', 'Giza'),
        ('Ankara', 'Ankara'),
        ('Beirut', 'Beirut'),
        ('Izmir', 'Izmir'),
        ('Damascus', 'Damascus'),
        ('Amman', 'Amman'),
        ('Kuwait', 'Kuwait'),
        ('Dubai', 'Dubai'),
        ('Abu_Dhabi', 'Abu Dhabi'),
        ('Doha', 'Doha'),
    )
    country=CountryField(blank_label="(select country)")
    city = models.CharField(max_length=50, choices=CITY_CHOICES)