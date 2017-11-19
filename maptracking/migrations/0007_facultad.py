# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maptracking', '0006_auto_20171119_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultad', models.CharField(choices=[('Ciencias Empresariales', 'Fce'), ('Ingenieria y Arquitectura', 'Fia'), ('Ciencias Humanas y Educacion', 'Fche'), ('Ciencias de la Salud', 'Fcs')], default='Ingenieria y Arquitectura', max_length=2)),
            ],
        ),
    ]
