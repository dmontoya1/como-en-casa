from django.db import models
from django.utils.text import slugify


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
    image = models.ImageField(
        'Imagen',
        upload_to='images/category',
        blank=True, null=True
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
