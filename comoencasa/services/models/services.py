from django.db import models


class Services(models.Model):
    """
    """

    name = models.CharField(
        'Nombre',
        max_length=255
    )
    code = models.CharField(
        'Código',
        max_length=15
    )
    description = models.TextField(
        'Descripción'
    )
    image = models.FileField(
        'Imagen',
        upload_to='services/',
        blank=True
    )


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "Servicio"
