from django.db import models
from estudiantes.models import Estudiante
from profesores.models import Profesor

# Create your models here.

class Clase(models.Model):
    asignature = models.CharField(default='', max_length=100)
    period = models.IntegerField()
    date = models.DateField(auto_now_add=True)


    estudiante = models.ManyToManyField(Estudiante, related_name="Clase")
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='Clase', null=True)


    def __str__(self):
        return self.asignature