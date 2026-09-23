from django.db import models



class City(models.Model):
    title = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
