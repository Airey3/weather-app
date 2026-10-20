from django.db import models



class City(models.Model):
    title = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.title 


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __srt__(self):
        return self.title 

    