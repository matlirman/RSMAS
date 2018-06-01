from django.db import models

# Create your models here.
class Site(models.Model):
    id = models.AutoField(primary_key=True)
    siteName = models.CharField(max_length = 200)
    siteDate = models.DateTimeField('Date of Observation')
    siteObserver = models.CharField(max_length = 100)
    nurseryName = models.CharField(max_length = 200)

class Structure(models.Model):
    id = models.AutoField(primary_key=True)
    nurseryName = models.CharField(max_length = 200)
    structureType = models.CharField(max_length = 200)
    structureAmount = models.IntegerField(default = 0)
    siteName = models.CharField(max_length = 200)
