# Generated by Django 2.0.10 on 2019-02-02 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='optionservices',
            options={'verbose_name': 'Opcion del servicio', 'verbose_name_plural': 'Opciones del servicio'},
        ),
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.FileField(blank=True, upload_to='services/', verbose_name='Imagen'),
        ),
    ]
