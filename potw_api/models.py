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
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField()
    ratings = models.FloatField()
    open_hours = models.CharField(max_length=100)
    closing_hours = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    socials = models.JSONField(default=dict, blank=True)
    image = models.CharField(max_length=200)

    class Meta:
        
        def __str__(self):
            return self.name
