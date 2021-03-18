from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=12, null=True, unique=True)


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
