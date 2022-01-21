from django.core import validators
from django.db import models

class Coordinate(models.Model):
    id = models.AutoField(primary_key=True)
    x = models.FloatField(validators=[validators.MinValueValidator(0.0)])
    y = models.FloatField(validators=[validators.MaxValueValidator(125.0)])
    z = models.FloatField()

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'