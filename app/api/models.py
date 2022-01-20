from django.db import models

class Coordinate(models.Model):
    id = models.AutoField(primary_key=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'