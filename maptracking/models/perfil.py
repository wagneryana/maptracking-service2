from django.db import models
from maptracking.models.catalgo_perfil import Catalogo_perfil
from maptracking.models.carrera import Carrera


class Perfil(models.Model):
    
    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre_perfil = models.CharField(max_length=60)
    descripcion = models.TextField()
    catalogo_perfil = models.ForeignKey(Catalogo_perfil)
    carrera = models.ForeignKey(Carrera)


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfils'
    
    def __str__(self):
        return '%s' % (self.nombre_perfil)
