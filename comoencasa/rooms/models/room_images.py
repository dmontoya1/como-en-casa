
from django.db import models


from .rooms import Room


class RoomImages(models.Model):
    """
    """

    room = models.ForeignKey(
        Room, 
        verbose_name='Habitacion',
        related_name='related_images', 
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Imagen',
        upload_to='images/rooms'
    )
    
    class Meta:
        verbose_name = 'Imagen de la habitacion'
        verbose_name_plural = 'Imagenes de la habitacion'
