from django.db import models

from .services import Services

class OptionServices(models.Model):
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
    name = models.CharField(
        'Nombre',
        max_length=255
    )
    option = models.CharField(
        'Opción de tiempo',
        max_length=2,
        choices=OPTIONS
    )
    value = models.CharField(
        'Valor',
        max_length=255
    )
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name