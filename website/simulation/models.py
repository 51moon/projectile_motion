from django.db import models

class SimulationData(models.Model):
    height = models.FloatField() # m
    velocity = models.FloatField() # m/s
    angle = models.FloatField() # °
    mass = models.FloatField() # kg
    cwArho = models.FloatField() # kg/m
    xmax = models.FloatField() # m
    ymax = models.FloatField() # m