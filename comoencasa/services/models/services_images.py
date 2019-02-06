from django.db import models

from .services import Services


class ServicesImage(models.Model):
    """
    """

    service = models.ForeignKey(
        Services,
        verbose_name='Experiencia',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.FileField(
        'Imagen',
        upload_to='images/services'
    )


    def __str__(self):
        return "Imagen de {}".format(self.service.name)
    

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'