# Generated by Django 3.2.9 on 2022-02-21 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
