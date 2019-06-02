from django.db import models

from .experiences import Experiences


class ExperiencesImage(models.Model):
    """
    """

    experience = models.ForeignKey(
        Experiences,
        verbose_name='Experiencia',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.FileField(
        'Imagen',
        upload_to='images/experiences'
    )


    def __str__(self):
        return "Imagen de {}".format(self.experience.name)
    

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
