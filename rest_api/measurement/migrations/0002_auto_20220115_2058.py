# Generated by Django 3.2.9 on 2022-01-15 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='updated_at',
        ),
    ]
