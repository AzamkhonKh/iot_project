from pyexpat import model
from statistics import mode
from django.db import models
# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=200)
    address_lat = models.DecimalField(max_digits=10, decimal_places=10)
    address_long = models.DecimalField(max_digits=10, decimal_places=10)

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.IntegerField()
    volume = models.FloatField(null=True)