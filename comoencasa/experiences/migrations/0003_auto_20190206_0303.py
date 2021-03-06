# Generated by Django 2.0.10 on 2019-02-06 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_experiencesimage_experiencesitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experiencesimage',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AddField(
            model_name='experiencesitems',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/experiences', verbose_name='Imagen'),
        ),
    ]
