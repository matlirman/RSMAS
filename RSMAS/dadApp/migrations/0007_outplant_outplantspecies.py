# Generated by Django 2.0.5 on 2018-06-03 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dadApp', '0006_auto_20180603_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outplant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=200)),
                ('outplantSite', models.CharField(max_length=200)),
                ('outplantDate', models.DateTimeField(verbose_name='Date of Collection')),
                ('outplantObserver', models.CharField(default='Anonymous', max_length=100)),
                ('outplantLat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('outplantLong', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='OutplantSpecies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('projectName', models.CharField(max_length=200)),
                ('outplantSite', models.CharField(max_length=200)),
                ('outplantDate', models.DateTimeField(verbose_name='Date of Collection')),
                ('outplantObserver', models.CharField(default='Anonymous', max_length=100)),
                ('outplantSpeciesType', models.CharField(max_length=200)),
                ('outplantSpeciesSmall', models.IntegerField(default=0)),
                ('outplantSpeciesMedium', models.IntegerField(default=0)),
                ('outplantSpeciesLarge', models.IntegerField(default=0)),
                ('outplantSpeciesXLarge', models.IntegerField(default=0)),
                ('outplantSpeciesTotal', models.IntegerField(default=0)),
                ('speciesOutplantMethod', models.CharField(max_length=100)),
            ],
        ),
    ]