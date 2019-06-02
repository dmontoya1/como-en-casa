from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    
    CEDULA_CIUDADANIA = 'CC'
    PASAPORTE = 'PA'
    TARJETA_IDENTIDAD = 'TI'
    CEDULA_EXTRANJERA = 'CE'

    DOCUMENT_TYPE = (
        (CEDULA_CIUDADANIA, 'Cédula de ciudadania'),
        (CEDULA_EXTRANJERA, 'Cédula de extranjería'),
        (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
        (PASAPORTE, 'Pasaporte')
    )
    document_type = models.CharField(
        "Tipo Documento",
        max_length=3,
        choices=DOCUMENT_TYPE,
        blank=True, null=True
    )
    document_id = models.CharField(
        "Número Documento",
        max_length=15,
        unique=True,
        blank=True, null=True
    )
    birth_date = models.DateField(
        'Fecha de nacimiento',
        auto_now_add=False,
        blank=True, null=True
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)