from django.db import models

class SimulationData(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    unit = models.CharField(max_length=20)