from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Screen(models.Model):
    name = models.CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    screen = models.ForeignKey(
        to=Screen, related_name='seats', on_delete=models.CASCADE)
    name = models.CharField(max_length=2)
    count = models.IntegerField()
    aisle = ArrayField(models.IntegerField())
    reserved = ArrayField(models.IntegerField())

    class Meta():
        unique_together = (('screen', 'name'),)

    def __str__(self):
        return f'Seat row {self.name} of screen {self.screen.name}'
