from django import forms
from .models import Site, Structure, Species, Maintenance, Damage
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
        choices.append(('none', '-------'))
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['siteName'].choices = choices

        nurseries = []
        queryTwo = Site.objects.values_list('nurseryName').distinct()
        nurseries.append(('none', '-------'))
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
        choices.append(('none', '-------'))
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
        choices.append(('none', '-------'))
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['speciesType'].choices = choices

class maintenanceForm(forms.Form):
    typeOfMaintenance = forms.ChoiceField(label = 'Maintenance Type', choices = [])
    otherMaintenance = forms.CharField(label = '(Other) New Type of Maintenance', required = False)
    dateOfMainenance = forms.DateTimeField(label = 'Date of Maintenance')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Maintenance.objects.values_list('typeOfMaintenance').distinct()
        choices.append(('none', '-------'))
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['typeOfMaintenance'].choices = choices

class damageForm(forms.Form):
    typeOfDamage = forms.ChoiceField(label = 'Damage Type', choices = [])
    otherDamage = forms.CharField(label = '(Other) New Type of Damage', required = False)
    dateOfDamage = forms.DateTimeField(label = 'Date of Damage')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        query = Damage.objects.values_list('typeOfDamage').distinct()
        choices.append(('none', '-------'))
        for x in query:
            choices.append((x[0], x[0]))
        choices.append(('Other', 'Other'))
        self.fields['typeOfDamage'].choices = choices
