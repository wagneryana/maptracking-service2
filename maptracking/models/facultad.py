from django.db import models

class Facultad(models.Model):
    FCE = 'Ciencias Empresariales'
    FIA = 'Ingenieria y Arquitectura'
    FCHE = 'Ciencias Humanas y Educacion'
    FCS = 'Ciencias de la Salud'
    FT = 'Teologia'
    FACULTAD_CHOICES = (
        (FCE, 'Ciencias Empresariales'),
        (FIA, 'Ingenieria y Arquitectura'),
        (FCHE, 'Ciencias Humanas y Educacion'),
        (FCS, 'Ciencias de la Salud'),
        (FT, 'Teologia'),
    )
    facultad = models.CharField(
        max_length=30,
        choices=FACULTAD_CHOICES,
        default=FIA,
    )

    def is_upperclass(self):
        return self.facultad in (self.FIA, self.FCE)