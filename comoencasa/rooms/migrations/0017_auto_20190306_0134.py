# Generated by Django 2.0.10 on 2019-03-06 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0016_room_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-id'], 'verbose_name': 'Habitación', 'verbose_name_plural': 'Habitaciones'},
        ),
    ]
