from django.db import models
from maptracking.models.competencia_general import Competencia_general


class Unidad_competencia(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    competencia_general = models.ForeignKey(Competencia_general)

    class Meta:
        verbose_name = 'Unidad_competencia'
        verbose_name_plural = 'Unidad_competencias'

    def __str__(self):
        return '%s' % (self.nombre)
