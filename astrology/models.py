from django.db import models

# Create your models here.
from django.db import models

class House(models.Model):
    house_no = models.IntegerField()
    
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
    rashi = models.CharField(max_length=50)
    results = models.TextField()

    def __str__(self):
        return f'House {self.house_no}'

