from django.contrib.auth import get_user_model

from django.db import models

from .category import Category
from .sectors import Sector

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
    price = models.IntegerField(
        'Precio de la habitacion',
        default=0,
    )
    room_sector = models.ForeignKey(
        Sector,
        verbose_name='Sector',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    short_description = models.CharField(
        'Descripcion Corta',
        max_length=255,
        default=''
    )
    description = models.TextField(
        'Descripción larga'
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
    available = models.BooleanField(
        'Habitacion disponible?',
        default=True
    )

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)

    def get_related_rooms(self):
        rooms = Room.objects.filter(category=self.category)
        return rooms

    class Meta:
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'
        ordering = ['-id']
