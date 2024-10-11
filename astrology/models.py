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

class House(models.Model):
    house_no = models.IntegerField()
    rashi = models.CharField(max_length=50, choices=rashi_options,default='None')

    
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
    
class DashaPhal(models.Model):
    planet = models.CharField(max_length=50, choices=planet_options)
    results = models.TextField()

    def __str__(self):
        return f'{self.planet}'
class AntarDashaPhal(models.Model):
    dasha = models.ForeignKey(DashaPhal, on_delete=models.CASCADE)
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