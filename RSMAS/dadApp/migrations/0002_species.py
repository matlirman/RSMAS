# Generated by Django 2.0.5 on 2018-06-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dadApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nurseryName', models.CharField(max_length=200)),
                ('speciesType', models.CharField(max_length=200)),
                ('speciesFragment', models.IntegerField(default=0)),
                ('speciesGenet', models.CharField(max_length=200)),
            ],
        ),
    ]
