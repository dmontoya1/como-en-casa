from django.db import models

from .experiences import Experiences


class ExperiencesOption(models.Model):
    """
    """

    experience = models.ForeignKey(
        Experiences,
        verbose_name='Experience',
        on_delete=models.CASCADE,
        related_name='related_options'
    )
    option = models.CharField(
        'Opcion',
        max_length=255
    )
    price = models.IntegerField(
        'Precio',
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.experience.name, self.option)

    class Meta:
        verbose_name = 'Opcion de la experiencia'
        verbose_name_plural = 'Opciones de la experiencia'
