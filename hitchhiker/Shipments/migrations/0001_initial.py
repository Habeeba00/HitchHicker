# Generated by Django 5.1 on 2024-09-08 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Befor', models.DateField()),
                ('Shipment_Name', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
                ('Weight', models.FloatField()),
                ('Price', models.FloatField()),
                ('Total_Price', models.FloatField(blank=True, null=True)),
                ('Total_Weight', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ship_from_location', to='Locations.locationmodel')),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ship_to_location', to='Locations.locationmodel')),
            ],
            options={
                'ordering': ['Date_Befor'],
            },
        ),
    ]
