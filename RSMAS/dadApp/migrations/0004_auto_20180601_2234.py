# Generated by Django 2.0.5 on 2018-06-01 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dadApp', '0003_damage_maintenance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenance',
            old_name='typeOfMaintanence',
            new_name='typeOfMaintenance',
        ),
    ]
