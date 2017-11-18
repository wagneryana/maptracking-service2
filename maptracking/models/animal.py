from django.db import models


class Animal(models.Model):

    name = models.CharField(max_length=60)
    sound = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name
