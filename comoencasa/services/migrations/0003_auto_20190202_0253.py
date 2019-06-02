# Generated by Django 2.0.10 on 2019-02-02 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190202_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionservices',
            name='name',
        ),
        migrations.RemoveField(
            model_name='optionservices',
            name='value',
        ),
        migrations.AddField(
            model_name='optionservices',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='optionservices',
            name='time',
            field=models.CharField(default='0', max_length=255, verbose_name='Tiempo'),
            preserve_default=False,
        ),
    ]
