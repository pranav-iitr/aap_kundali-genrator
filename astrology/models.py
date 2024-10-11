from django.db import models

# Create your models here.
from django.db import models

planet_options = [
    ('Surya', 'Surya'),
    ('Moon', 'Moon'),
    ('Mangal', 'Mangal'),
    ('Budh', 'Budh'),
    ('Guru', 'Guru'),
    ('Shukra', 'Shukra'),
    ('Shani', 'Shani'),
    ('Rahu', 'Rahu'),
    ('Ketu', 'Ketu'),
]

rashi_options = [
    ('None', 'None'),
    ('Mesh', 'Mesh'),
    ('Vrishabh', 'Vrishabh'),
    ('Mithun', 'Mithun'),
    ('Kark', 'Kark'),
    ('Simha', 'Simha'),
    ('Kanya', 'Kanya'),
    ('Tula', 'Tula'),
    ('Vrischik', 'Vrischik'),
    ('Dhanu', 'Dhanu'),
    ('Makar', 'Makar'),
    ('Kumbh', 'Kumbh'),
    ('Meen', 'Meen'),
]

naksatra_options = [
    ('None', 'None'),
    ('Ashwini', 'Ashwini'),
    ('Bharani', 'Bharani'),
    ('Kritika', 'Kritika'),
    ('Rohini', 'Rohini'),
    ('Mrigashira', 'Mrigashira'),
    ('Ardra', 'Ardra'),
    ('Punarvasu', 'Punarvasu'),
    ('Pushya', 'Pushya'),
    ('Ashlesha', 'Ashlesha'),
    ('Magha', 'Magha'),
    ('Purva Phalguni', 'Purva Phalguni'),
    ('Uttara Phalguni', 'Uttara Phalguni'),
    ('Hasta', 'Hasta'),
    ('Chitra', 'Chitra'),
    ('Swati', 'Swati'),
    ('Vishakha', 'Vishakha'),
    ('Anuradha', 'Anuradha'),
    ('Jyeshtha', 'Jyeshtha'),
    ('Mula', 'Mula'),
    ('Purva Ashadha', 'Purva Ashadha'),
    ('Uttara Ashadha', 'Uttara Ashadha'),
    ('Shravana', 'Shravana'),
    ('Dhanishta', 'Dhanishta'),
    ('Shatabhisha', 'Shatabhisha'),
    ('Purva Bhadrapada', 'Purva Bhadrapada'),
    ('Uttara Bhadrapada', 'Uttara Bhadrapada'),
    ('Revati', 'Revati'),
]

class House(models.Model):
    house_no = models.IntegerField()
    rashi = models.CharField(max_length=50, choices=rashi_options,default='None')
    nakshtra = models.CharField(max_length=50, choices=naksatra_options,default='None')
    lagna_raashi = models.CharField(max_length=50, choices=rashi_options,default='None')
    lagna_planet = models.CharField(max_length=50, choices=planet_options,default='None')

    
    # Planet presence booleans
    surya_present = models.BooleanField(default=False)
    moon_present = models.BooleanField(default=False)
    mangal_present = models.BooleanField(default=False)
    budh_present = models.BooleanField(default=False)
    guru_present = models.BooleanField(default=False)
    shukra_present = models.BooleanField(default=False)
    shani_present = models.BooleanField(default=False)
    rahu_present = models.BooleanField(default=False)
    ketu_present = models.BooleanField(default=False)
    
    # Drishti (aspect) booleans
    surya_drishti = models.BooleanField(default=False)
    moon_drishti = models.BooleanField(default=False)
    mangal_drishti = models.BooleanField(default=False)
    budh_drishti = models.BooleanField(default=False)
    guru_drishti = models.BooleanField(default=False)
    shukra_drishti = models.BooleanField(default=False)
    shani_drishti = models.BooleanField(default=False)
    rahu_drishti = models.BooleanField(default=False)
    ketu_drishti = models.BooleanField(default=False)

    # Rashi field
    results = models.TextField()

    def __str__(self):
        return f'House {self.house_no}'
    
class MahaDashaPhal(models.Model):
    planet = models.CharField(max_length=50, choices=planet_options)
    results = models.TextField()

    def __str__(self):
        return f'{self.planet}'
class AntarDashaPhal(models.Model):
    dasha = models.ForeignKey(MahaDashaPhal, on_delete=models.CASCADE)
    planet = models.CharField(max_length=50, choices=planet_options)
    results = models.TextField()

    def __str__(self):
        return f'{self.planet} in {self.dasha}'
class PratyantarDashaPhal(models.Model):
    antardasha = models.ForeignKey(AntarDashaPhal, on_delete=models.CASCADE)
    planet = models.CharField(max_length=50, choices=planet_options)
    results = models.TextField()

    def __str__(self):
        return f'{self.planet} in {self.antardasha} in {self.antardasha.dasha}'