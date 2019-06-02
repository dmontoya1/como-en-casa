from django.db import models

from .services import Services

class ServicesOption(models.Model):
    """
    """

    HOURS = 'HO'
    DAYS = 'DA'
    WEEKS = 'WE'
    MONTHS = 'MO'

    OPTIONS = (
        (HOURS, 'Horas'),
        (DAYS, 'Dias'),
        (WEEKS, 'Semanas'),
        (MONTHS, 'Meses'),
    )

    service = models.ForeignKey(
        Services,
        verbose_name='Servicio',
        on_delete=models.CASCADE,
        related_name='related_options'
    )
    time = models.CharField(
        'Tiempo',
        max_length=255
    )
    option = models.CharField(
        'Opción de tiempo',
        max_length=2,
        choices=OPTIONS
    )
    price = models.IntegerField(
        'Precio',
    )
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "{} ({} {})".format(self.service.name, self.time, self.get_option_display())

    
    class Meta:
        verbose_name = 'Opcion del servicio'
        verbose_name_plural = 'Opciones del servicio'
