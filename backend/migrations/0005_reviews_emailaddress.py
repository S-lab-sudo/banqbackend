# Generated by Django 5.0.2 on 2024-03-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_reservation_timeofvisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='emailaddress',
            field=models.EmailField(default=0, max_length=254),
        ),
    ]
