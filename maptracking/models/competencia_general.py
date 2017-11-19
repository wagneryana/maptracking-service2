from django.db import models
from maptracking.models.perfil import Perfil


class Competencia_general(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    perfil = models.ForeignKey(Perfil)

    class Meta:
        verbose_name = 'Competencia_general'
        verbose_name_plural = 'Competencia_generals'

    def __str__(self):
        return '%s' % (self.nombre)
