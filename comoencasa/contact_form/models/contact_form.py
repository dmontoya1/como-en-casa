
from django.db import models


class ContactForm(models.Model):
    """Modelo para administrar los formularios de contacto
    """

    PETICION = 'PE'
    QUEJA = 'QU'
    PREGUNTA = 'PR'
    RECLAMO = 'RE'
    SUGERENCIA = 'SU'
    FELICITACION = 'FE'

    TYPES = (
        (PETICION, 'Petición'),
        (QUEJA, 'Queja'),
        (PREGUNTA, 'Pregunta'),
        (RECLAMO, 'Reclamo'),
        (SUGERENCIA, 'Sugerencia'),
        (FELICITACION, 'Felicitación')
    )

    full_name = models.CharField(
        "Nombre completo",
        max_length=255
    )
    email = models.CharField(
        "Correo",
        max_length=255
    )
    contact_type = models.CharField(
        "Motivo",
        max_length=2,
        choices=TYPES,
    )
    date = models.DateTimeField(
        "Fecha de envío",
        auto_now_add=True
    )
    message = models.TextField(
        "Mensaje",
    )


    def __str__(self):
        return "Formulario de contacto de %s" % (self.full_name)


    class Meta:
        verbose_name = "Formulario de contacto"
        verbose_name_plural = "Formularios de contacto"
