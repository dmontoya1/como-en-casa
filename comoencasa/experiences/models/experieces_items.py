from django.db import models

from .experiences import Experiences


class ExperiencesItems(models.Model):
    """
    """

    experience = models.ForeignKey(
        Experiences,
        verbose_name='Experiencia',
        on_delete=models.CASCADE,
        related_name='items'
    )
    name = models.CharField(
        'Nombre',
        max_length=255,
    )
    image = models.FileField(
        'Imagen',
        upload_to='images/experiences',
        blank=True, null=True,
    )

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Item'
