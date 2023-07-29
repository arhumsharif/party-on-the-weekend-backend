from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    email = models.EmailField(unique=True, db_index=True)
    genres = ArrayField(models.CharField(max_length=100))
    is_active = models.BooleanField(default=True)
    credentials = models.CharField(max_length=200)

    class Meta:

        def __str__(self):
            return self.name

class Place(models.Model):
    name = models.CharField(max_length=200, null=False)
    genres = ArrayField(models.CharField(max_length=100))
    longitude = models.FloatField(null= True, blank = True)
    latitude = models.FloatField(null= True, blank = True)
    description = models.TextField(null= True, blank = True)
    ratings = models.FloatField(null= True, blank = True)
    open_hours = models.CharField(max_length=100,null= True, blank = True)
    closing_hours = models.CharField(max_length=100,null= True, blank = True)
    address = models.CharField(max_length=200,null= True, blank = True)
    website = models.URLField(max_length=200,null= True, blank = True)
    socials = models.JSONField(default=dict, blank=True, null = True)
    image = models.CharField(max_length=200, null= True, blank = True)

    class Meta:
        
        def __str__(self):
            return self.name
