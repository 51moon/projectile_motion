from django.db import models

class SimulationData(models.Model):
    height = models.FloatField(default=1) # m
    velocity = models.FloatField(default=20) # m/s
    angle = models.FloatField(default=40) # °
    mass = models.FloatField(default=1) # kg
    cwArho = models.FloatField(default=0.5) # kg/m
    xmax = models.FloatField(default=6) # m
    ymax = models.FloatField(default=4) # m