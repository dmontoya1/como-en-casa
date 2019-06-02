from django.db import models

from .category import Category

class CategoryServices(models.Model):
    """
    """

    name = models.CharField(
        'Nombre',
        max_length=255
    )
    image = models.FileField(
        'Imagen',
        upload_to='images/category/services/'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Categoria',
        related_name="related_services",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Servicio de Categoria"
        verbose_name_plural = "Servicios de Categoria"

    def __str__(self):
        return self.name
