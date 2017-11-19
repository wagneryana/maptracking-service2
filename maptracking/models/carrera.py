from django.db import models
from maptracking.models.escuela import Escuela


class Carrera(models.Model):
    
    nombre_carrera = models.CharField(max_length = 60)
    descripcion = models.TextField()
    escuela = models.ForeignKey(Escuela)


    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return '%s' % (self.nombre_carrera)
