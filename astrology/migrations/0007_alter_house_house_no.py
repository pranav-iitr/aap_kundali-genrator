# Generated by Django 5.1.2 on 2024-10-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrology', '0006_house_element_house_nakshtra_pada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='house_no',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1),
        ),
    ]
