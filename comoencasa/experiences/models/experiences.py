from django.db import models


class Experiences(models.Model):
    """
    """

    name = models.CharField(
        'Nombre',
        max_length=255,
    )
    description = models.TextField(
        'Descripcion',
    )
    location = models.CharField(
        'Ubicación',
        max_length=255
    )
    total_time = models.CharField(
        'Tiempo total',
        max_length=255
    )
    price = models.IntegerField(
        'Precio',
        default=0
    )

    short_description = models.CharField(
        'Descripcion corta',
        max_length=255,
        default=''
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Experiencia'
