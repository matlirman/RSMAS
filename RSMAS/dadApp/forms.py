from django import forms
from .models import Site, Structure, Species, Maintenance, Damage, Outplant, OutplantSpecies, Collection, CollectionSpecies
from django.forms.formsets import formset_factory

class siteForm(forms.Form):
    siteName = forms.ChoiceField(label = 'Site Name', choices = [])
    otherSite =  forms.CharField(label = '(Other) New Site', required = False)
    siteDate = forms.DateTimeField(label = 'Date')
    siteObserver = forms.CharField(label = 'Your Name', max_length = 100)
    siteNursery = forms.ChoiceField(label = 'Nursery Name', choices = [])
    otherNursery = forms.CharField(label = '(Other) New Nursery', required = False)
    typeofReport = forms.ChoiceField( label = 'Type of Report', choices = [('nursery', 'Nursery Report'), ('maintenance', 'Maintenance Report'), ('damages', 'Damages Report')])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Site.objects.values_list('siteName').distinct()

        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['siteName'].choices = choices
        nurseries = []
        queryTwo = Site.objects.values_list('nurseryName').distinct()
        for x in queryTwo:
            nurseries.append((x[0], x[0]))
        nurseries.append(('Other', 'Other'))
        self.fields['siteNursery'].choices = nurseries


class numberOfStructuresForm(forms.Form):
    numberOfStructures = forms.IntegerField(label = 'Number of structures to report', min_value = 0)

class structureForm(forms.Form):
    structureType = forms.ChoiceField(label = 'Structure Type', choices = [])
    otherStructure = forms.CharField(label = '(Other) New Structure', required = False)
    numberOfSpecificStructures = forms.IntegerField(label = 'Number of Specific Structures', min_value = 0)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Structure.objects.values_list('structureType').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['structureType'].choices = choices

class numberOfSpeciesForm(forms.Form):
    numberOfSpecies = forms.IntegerField(label = 'Number of species to report' , min_value = 0)

class speciesForm(forms.Form):
    speciesType = forms.ChoiceField(label = 'Species Type', choices = [])
    otherSpecies = forms.CharField(label = '(Other) New Species', required = False)
    numberOfSmallFragments = forms.IntegerField(label = 'Number of Small Fragments', min_value = 0)
    numberOfMediumFragments = forms.IntegerField(label = 'Number of Medium Fragments', min_value = 0)
    numberOfLargeFragments = forms.IntegerField(label = 'Number of Large Fragments', min_value = 0)
    numberOfXLargeFragments = forms.IntegerField(label = 'Number of Extra Large Fragments', min_value = 0)
    numberOfGenets = forms.IntegerField(label = 'Number of Genets', min_value = 0)
    percentOfDead = forms.IntegerField(label = 'Percentage of 100% mortality', min_value = 0, max_value = 100)
    percentOfDiseased = forms.IntegerField(label = 'Percentage of Diseased', min_value = 0, max_value = 100)
    percentOfBleached = forms.IntegerField(label = 'Percentage of Bleached', min_value = 0, max_value = 100)
    percentOfBroken = forms.IntegerField(label = 'Percentage of Broken', min_value = 0, max_value = 100)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Species.objects.values_list('speciesType').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['speciesType'].choices = choices

class maintenanceForm(forms.Form):
    typeOfMaintenance = forms.ChoiceField(label = 'Maintenance Type', choices = [])
    otherMaintenance = forms.CharField(label = '(Other) New Type of Maintenance', required = False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Maintenance.objects.values_list('typeOfMaintenance').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['typeOfMaintenance'].choices = choices

class damageForm(forms.Form):
    typeOfDamage = forms.ChoiceField(label = 'Damage Type', choices = [])
    otherDamage = forms.CharField(label = '(Other) New Type of Damage', required = False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Damage.objects.values_list('typeOfDamage').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['typeOfDamage'].choices = choices

class outplantForm(forms.Form):
    projectName = forms.CharField(label = 'Project Name')
    outplantSite = forms.ChoiceField(label = 'Outplant Site', choices = [])
    otherOutplantSite = forms.CharField(label = '(Other) Outplant Site')
    outplantDate = forms.DateTimeField(label = 'Date')
    outplantObserver = forms.CharField(label = 'Your Name', max_length = 100)
    outplantLat = forms.DecimalField(label = 'Outplant Site Latitude Coordinates', max_digits=9, decimal_places=6)
    outplantLong = forms.DecimalField(label = 'Outplant Site Longitude Coordinates',max_digits=9, decimal_places=6)
    numberOfSpeciesPlanted = forms.IntegerField(label = 'Number of Species Outplanted', min_value = 0)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Outplant.objects.values_list('outplantSite').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['outplantSite'].choices = choices


class speciesOutplantForm(forms.Form):
    speciesType = forms.ChoiceField(label = 'Species Type', choices = [])
    otherSpecies = forms.CharField(label = '(Other) New Species', required = False)
    numberOfSmallFragments = forms.IntegerField(label = 'Number of Small Fragments Outplanted', min_value = 0)
    numberOfMediumFragments = forms.IntegerField(label = 'Number of Medium Fragments Outplanted', min_value = 0)
    numberOfLargeFragments = forms.IntegerField(label = 'Number of Large Fragments Outplanted', min_value = 0)
    numberOfXLargeFragments = forms.IntegerField(label = 'Number of Extra Large Fragments Outplanted', min_value = 0)
    methodOfOutplant = forms.ChoiceField(label = 'Type of outplant method', choices = [])
    otherMethodOfOutplant = forms.CharField(label = '(Other) Outplant Method', required = False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = OutplantSpecies.objects.values_list('outplantSpeciesType').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['speciesType'].choices = choices
        choicesTwo = []
        queryTwo = OutplantSpecies.objects.values_list('speciesOutplantMethod').distinct()
        for x in queryTwo:
            choicesTwo.append((x[0], x[0]))
        choicesTwo.append(('Other', 'Other'))
        self.fields['methodOfOutplant'].choices = choicesTwo


class collectionForm(forms.Form):
    collectionSite = forms.ChoiceField(label = 'Collection Site', choices = [])
    otherCollectionSite = forms.CharField(label = '(Other) Collection Site')
    collectionDate = forms.DateTimeField(label = 'Date')
    collectionObserver = forms.CharField(label = 'Your Name', max_length = 100)
    collectionLat = forms.DecimalField(label = 'Collection Site Latitude Coordinates', max_digits=9, decimal_places=6)
    collectionLong = forms.DecimalField(label = 'Collection Site Longitude Coordinates',max_digits=9, decimal_places=6)
    collectionDepth = forms.IntegerField(label = 'Depth of Site (ft)', min_value = 0)
    numberOfSpeciesCollected = forms.IntegerField(label = 'Number of Species Collected', min_value = 0)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Collection.objects.values_list('collectionSite').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['collectionSite'].choices = choices


class collectionSpeciesForm(forms.Form):
    collectionSpecies = forms.ChoiceField(label = 'Species Type', choices = [])
    otherCollectionSpecies = forms.CharField(label = '(Other) New Species', required = False)
    collectionColonySize = forms.IntegerField(label = 'Colony Size (cm)', min_value = 0)
    collectionFragments = forms.IntegerField(label = 'Number of Fragments Collected', min_value = 0)
    collectionTLE = forms.IntegerField(label = 'TLE Collected', min_value = 0)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = CollectionSpecies.objects.values_list('collectionSpecies').distinct()
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['collectionSpecies'].choices = choices
