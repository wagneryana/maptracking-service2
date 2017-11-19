from django.db import models


class Escuela(models.Model):
    ANI = 'ani'
    CGT = 'cgt'
    MH = 'mh'
    NH = 'nh'
    Enf = 'enf'
    Ps = 'ps'
    CC = 'cc'
    EIP = 'eip'
    EP = 'ep'
    EMA = 'ema'
    EF = 'ef'
    EMF = 'emf'
    EABQ = 'eab'
    IS = 'is'
    IA = 'ia'
    IIA = 'iia'
    IC = 'ic'
    ESCUELA_CHOICES = (
        (ANI, 'Administracion y Negocios Internacionales'),
        (CGT, 'Contabilidad y Gestion Tributaria'),
        (MH, 'Medicina Humana'),
        (NH, 'Nutricion Humana'),
        (Enf, 'Enfermeria'),
        (Ps, 'Psicologia'),
        (CC, 'Ciencias de la Comunicacion'),
        (EIP, 'Educacion de Linguistica e Ingles'),
        (EP, 'Educacion Primaria'),
        (EMA, 'Educacion Musical y Artes'),
        (EF, 'Educacion Fisica'),
        (EMF, 'Educacion Matematica y Fisica'),
        (EABQ, 'Educacion Ambiental, Biologia y Quimica'),
        (IS, 'Ingenieria de Sistemas'),
        (IA, 'Ingenieria Ambiental'),
        (IIA, 'Ingenieria de Industrias Alimentarias'),
        (IC, 'Ingenieria Civil'),
    )
    escuela = models.CharField(
        max_length=30,
        choices=ESCUELA_CHOICES,
        default=IS,
    )

    def is_upperclass(self):
        return self.escuela in (self.IS, self.IC)
