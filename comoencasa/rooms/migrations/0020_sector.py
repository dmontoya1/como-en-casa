# Generated by Django 2.0.10 on 2019-06-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0019_auto_20190306_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='images/sectors', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
            },
        ),
    ]
