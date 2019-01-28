from django.db import models

from .category import Category

class CategoryBenefits(models.Model):
    """
    """

    name = models.CharField(
        'Nombre',
        max_length=255
    )
    image = models.FileField(
        'Imagen',
        upload_to='images/category/benefits/'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Categoria',
        related_name="related_benefits",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Beneficio de Categoria"
        verbose_name_plural = "Beneficios de Categoria"

    def __str__(self):
        return self.name
