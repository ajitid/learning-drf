from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Screen(models.Model):
    name = models.CharField(max_length=40, primary_key=True)


class Seat(models.Model):
    screen = models.ForeignKey(to=Screen, on_delete=models.CASCADE)
    name = models.CharField(max_length=2)
    count = models.IntegerField()
    aisle = ArrayField(models.IntegerField())
    reserved = ArrayField(models.IntegerField())
