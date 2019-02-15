# Generated by Django 2.0.10 on 2019-02-15 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mision', models.TextField(verbose_name='Mision')),
                ('mision_image', models.ImageField(upload_to='images/company/', verbose_name='Imagen Mision')),
                ('vision', models.TextField(verbose_name='Vision')),
                ('vision_image', models.ImageField(upload_to='images/company/', verbose_name='Imagen Vision')),
                ('corporative_values', models.TextField(verbose_name='Valores Corporativos')),
                ('corporative_values_image', models.ImageField(upload_to='images/company/', verbose_name='Imagen Valores Corporativos')),
            ],
            options={
                'verbose_name': 'Informacion Como En Casa',
            },
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_type', models.CharField(choices=[('TC', 'Términos y condiciones'), ('PP', 'Políticas de privacidad'), ('CO', 'Cookies')], max_length=2, unique=True, verbose_name='Tipo de Política')),
                ('text', models.TextField(verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Politica',
            },
        ),
    ]
