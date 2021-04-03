from django.db import models

# Create your models here.

from django.db import models

class Restaurant(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Dish(models.Model):
    ticker  = models.CharField(max_length=200)
    exchange = models.CharField(max_length=200)
    signal = models.CharField(max_length=200)
    volume = models.FloatField()
    volumeindikator = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    orgm = models.CharField(max_length=200)
    status = models.CharField(max_length=200,default="open")
    previoustrade = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT)

