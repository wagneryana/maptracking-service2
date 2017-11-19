from django.db import models


class Catalogo_perfil(models.Model):
    
    codigo = models.CharField(max_length=10, null=True, blank=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    

    class Meta:
        verbose_name = 'Catalogo_perfil'
        verbose_name_plural = 'Catalogo_perfils'

    def __str__(self):
        return '%s' % (self.nombre)
