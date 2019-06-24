
from django.db import models


class Sector(models.Model):

    name = models.CharField(
        'Nombre',
        max_length=255
    )
    image = models.ImageField(
        'Imagen',
        upload_to='images/sectors'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
