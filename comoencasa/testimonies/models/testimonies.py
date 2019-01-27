from django.db import models

# Create your models here.

class Testimonies(models.Model):
    """
    """

    name = models.CharField(
        'Nombre usuario',
        max_length=255
    )
    profesion = models.CharField(
        'Profesion',
        max_length=255
    )
    detail = models.TextField(
        'Detalle'
    )
    image = models.ImageField(
        'Imagen usuario',
        upload_to='testimonios/'
    )

    def __str__(self):
        return "Testimonio de %s" % (self.name)

    
    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
