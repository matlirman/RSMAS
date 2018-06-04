from django.db import models

# Create your models here.
class Site(models.Model):
    id = models.AutoField(primary_key=True)
    siteName = models.CharField(max_length = 200)
    siteDate = models.DateTimeField('Date of Observation')
    siteObserver = models.CharField(max_length = 100, default = 'Anonymous')
    nurseryName = models.CharField(max_length = 200)

class Structure(models.Model):
    id = models.AutoField(primary_key=True)
    nurseryName = models.CharField(max_length = 200)
    structureType = models.CharField(max_length = 200)
    structureAmount = models.IntegerField(default = 0)
    siteObserver = models.CharField(max_length = 100, default = 'Anonymous')
    siteName = models.CharField(max_length = 200)

class Species(models.Model):
    id = models.AutoField(primary_key=True)
    nurseryName = models.CharField(max_length = 200)
    speciesType = models.CharField(max_length = 200)
    speciesSmall = models.IntegerField(default = 0)
    speciesMedium = models.IntegerField(default = 0)
    speciesLarge = models.IntegerField(default = 0)
    speciesXLarge = models.IntegerField(default = 0)
    speciesFragment = models.IntegerField(default = 0)
    speciesGenet = models.CharField(max_length = 200)
    percent100Dead = models.IntegerField(default = 0)
    percentOfDiseased = models.IntegerField(default = 0)
    percentOfBleached = models.IntegerField(default = 0)
    percentOfBroken = models.IntegerField(default = 0)
    siteObserver = models.CharField(max_length = 100, default = 'Anonymous')

class Maintenance(models.Model):
    id = models.AutoField(primary_key=True)
    siteObserver = models.CharField(max_length = 100, default = 'Anonymous')
    siteName = models.CharField(max_length = 200)
    nurseryName = models.CharField(max_length = 200)
    typeOfMaintenance = models.CharField(max_length = 200)
    maintenanceDate = models.DateTimeField('Date of Maintenance')

class Damage(models.Model):
    id = models.AutoField(primary_key=True)
    siteObserver = models.CharField(max_length = 100, default = 'Anonymous')
    siteName = models.CharField(max_length = 200)
    nurseryName = models.CharField(max_length = 200)
    typeOfDamage = models.CharField(max_length = 200)
    DamageObservedDate = models.DateTimeField('Date of Observed Damage')

class Outplant(models.Model):
    id = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length = 200)
    outplantSite = models.CharField(max_length = 200)
    outplantDate = models.DateTimeField('Date of Collection')
    outplantObserver = models.CharField(max_length = 100, default = 'Anonymous')
    outplantLat = models.DecimalField(max_digits=9, decimal_places=6)
    outplantLong = models.DecimalField(max_digits=9, decimal_places=6)

class OutplantSpecies(models.Model):
    id = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length = 200)
    outplantSite = models.CharField(max_length = 200)
    outplantDate = models.DateTimeField('Date of Collection')
    outplantObserver = models.CharField(max_length = 100, default = 'Anonymous')
    outplantSpeciesType = models.CharField(max_length = 200)
    outplantSpeciesSmall = models.IntegerField(default = 0)
    outplantSpeciesMedium = models.IntegerField(default = 0)
    outplantSpeciesLarge = models.IntegerField(default = 0)
    outplantSpeciesXLarge = models.IntegerField(default = 0)
    outplantSpeciesTotal = models.IntegerField(default = 0)
    speciesOutplantMethod = models.CharField(max_length = 100)

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    collectionSite = models.CharField(max_length = 200)
    collectionLat = models.DecimalField(max_digits=9, decimal_places=6)
    collectionLong = models.DecimalField(max_digits=9, decimal_places=6)
    collectionObserver = models.CharField(max_length = 100, default = 'Anonymous')
    collectionDate = models.DateTimeField('Date of Collection')
    collectionDepth = models.IntegerField(default = 0)

class CollectionSpecies(models.Model):
    id = models.AutoField(primary_key=True)
    collectionSite = models.CharField(max_length = 200)
    collectionDate = models.DateTimeField('Date of Collection')
    collectionObserver = models.CharField(max_length = 100, default = 'Anonymous')
    collectionSpecies = models.CharField(max_length = 200)
    collectionColonySize = models.IntegerField(default = 0)
    collectionFragments = models.IntegerField(default = 0)
    collectionTLE = models.IntegerField(default = 0)
