from django.db import models


class Category(models.Model):
    """
    """

    name = models.CharField(
        'Nombre',
        max_length=255
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Tipo de acomodacion',
        null=True, blank=True, 
        related_name="related_categories",
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        'Descripcion'
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
