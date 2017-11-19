from django.db import models


class Escuela(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'

    def __str__(self):
        return '%s' % (self.nombre)
