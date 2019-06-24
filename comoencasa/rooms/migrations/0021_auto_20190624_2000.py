# Generated by Django 2.0.10 on 2019-06-24 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0020_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='sector',
        ),
        migrations.AddField(
            model_name='room',
            name='room_sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.Sector'),
        ),
    ]
