from django.db import models

class Calificacion(models.Model):
    materia = models.CharField(max_length=100)
    cal = models.FloatField()

    def __str__(self):
        return self.materia
