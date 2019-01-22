
from django.db import models


from .rooms import Room


class RoomItems(models.Model):
    """
    """

    room = models.ForeignKey(
        Room, 
        verbose_name='Habitacion',
        related_name='related_items', 
        on_delete=models.CASCADE
    )
    logo = models.FileField(
        'Logo',
        upload_to='logos/rooms'
    )
    name = models.CharField(
        'Nombre',
        max_length=255
    )
    value = models.CharField(
        'Valor',
        max_length=255
    )

    class Meta:
        verbose_name = 'Item de la habitacion'
        verbose_name_plural = 'Items de la habitacion'