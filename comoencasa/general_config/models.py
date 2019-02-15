from django.db import models


class Police(models.Model):
    """
    clase para las politicas de la plataforma
    """

    TERMINOS_CONDICIONES = 'TC'
    POLITICAS_PRIVACIDAD = 'PP'
    COOKIES = 'CO'

    POLICE_TYPE = (
        (TERMINOS_CONDICIONES, 'Términos y condiciones'),
        (POLITICAS_PRIVACIDAD, 'Políticas de privacidad'),
        (COOKIES, 'Cookies')
    )

    police_type = models.CharField("Tipo de Política", max_length=2, choices=POLICE_TYPE,
                                   unique=True)
    text = models.TextField("Texto")

    def __str__(self):
        return "%s" % (self.police_type)

    class Meta:
        verbose_name = "Politica"


class CompanyInfo(models.Model):
    """
    """
    about = models.TextField(
        'Nuestra Empresa',
        default='',
    )
    mision = models.TextField(
        'Mision',
    )
    mision_image = models.ImageField(
        'Imagen Mision',
        upload_to='images/company/'
    )
    vision = models.TextField(
        'Vision'
    )
    vision_image = models.ImageField(
        'Imagen Vision',
        upload_to='images/company/'
    )
    corporative_values = models.TextField(
        'Valores Corporativos'
    )
    corporative_values_image = models.ImageField(
        'Imagen Valores Corporativos',
        upload_to='images/company/'
    )

    def __str__(self):
        return "Informacion"

    class Meta:
        verbose_name = "Informacion Como En Casa" 
