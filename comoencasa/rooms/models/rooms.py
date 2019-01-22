from django.contrib.auth import get_user_model

from django.db import models

from .category import Category

User = get_user_model()

class Room(models.Model):
    """
    """

    name = models.CharField(
        'Nombre del anuncio',
        max_length=255, 
    )
    code = models.CharField(
        'Código del anuncio',
        max_length=255
    )
    description = models.TextField(
        'Descripción'
    )
    agent = models.ForeignKey(
        User,
        verbose_name='Agente',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Categoria',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )


    def __str__(self):
        return '{} ({})'.format(self.name, self.code)
    

    class Meta:
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'
