from django.shortcuts import render, redirect, reverse
from .forms import siteForm, structureForm, numberOfStructuresForm, numberOfSpeciesForm, speciesForm, maintenanceForm, damageForm
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from .models import Site, Structure, Species
from math import *



# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'dadApp/index.html')

def siteInput(request):
    formOne = siteForm(request.POST or None)
    if formOne.is_valid():
        request.session['nurseryName'] = formOne.cleaned_data['siteNursery']
        request.session['siteName'] = formOne.cleaned_data['siteName']
        request.session['siteObserver'] = formOne.cleaned_data['siteObserver']

        if formOne.cleaned_data['typeofReport'] == 'nursery':
            if formOne.cleaned_data['siteName'] == 'Other' or formOne.cleaned_data['siteName'] == 'none':
                siteName = formOne.cleaned_data['otherSite']
            else:
                siteName = formOne.cleaned_data['siteName']
            siteDate = formOne.cleaned_data['siteDate']
            siteObserver = formOne.cleaned_data['siteObserver']
    # check if he wants a pull down menu for site name
            if formOne.cleaned_data['siteNursery'] == 'Other' or formOne.cleaned_data['siteNursery'] == 'none':
                nurseryName = formOne.cleaned_data['otherNursery']
            else:
                nurseryName = formOne.cleaned_data['siteNursery']
            p = Site(siteName=siteName, siteDate=siteDate, siteObserver=siteObserver, nurseryName = nurseryName)
            p.save()
            return redirect('structure')

        elif formOne.cleaned_data['typeofReport'] == 'maintenance':
            return redirect('maintenance')
        else:
            return redirect('damage')
    # for p in Person.objects.raw('SELECT * FROM myapp_person'):
    # x = Person.objects.raw('SELECT * FROM myapp_person')[0]
    return render(request, 'dadApp/site.html', {'formOne' : formOne})
    # return HttpResponse("Hello, world. You're at the polls index.")

# def structure2(request):
#     formset = []
#     nurseryName = request.session.get('nurseryName')
#     siteName = request.session.get('siteName')
#     message = ''
#
#     form = numberOfStructuresForm(request.POST or None)
#     if form.is_valid():
#         numberOfStructures = form.cleaned_data['numberOfStructures']
#         if int(numberOfStructures) == 0:
#             return redirect('species')
#         message = "Please input the " + str(numberOfStructures) + " Structures"
#         structureFormset= formset_factory(structureForm, extra = int(numberOfStructures))
#         formset = structureFormset(request.POST or None)
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data['structureType'] == 'Other' or form.cleaned_data['structureType'] == 'none':
#                     structureType = form.cleaned_data['otherStructure']
#                 else:
#                     structureType = form.cleaned_data['structureType']
#                 numberOfSpecificStructures = form.cleaned_data['numberOfSpecificStructures']
#                 p = Structure(nurseryName = nurseryName, structureType = structureType, structureAmount = numberOfSpecificStructures, siteName = siteName)
#                 p.save()
#             return redirect('species')
#
#     return render(request, 'dadApp/structure.html', {'nurseryName' : nurseryName , 'siteName' : siteName , 'form' : form , 'message' : message, 'formset' : formset})




def structure(request):
    nurseryName = request.session.get('nurseryName')
    siteName = request.session.get('siteName')

    form = numberOfStructuresForm(request.POST or None)
    if form.is_valid():
        numberOfStructures = form.cleaned_data['numberOfStructures']
        request.session['numberOfStructures'] = numberOfStructures
        return redirect('specificStructure')
    else:
        print("fuck that")
    return render(request, 'dadApp/structure.html', {'nurseryName' : nurseryName , 'siteName' : siteName , 'form' : form})


def specificStructure(request):
    nurseryName = request.session.get('nurseryName')
    siteName = request.session.get('siteName')
    numberOfStructures = request.session.get('numberOfStructures')
    message = ''
    if int(numberOfStructures) == 0:
        return redirect('species')
    message = "Please input the " + str(numberOfStructures) + " Structures"
    structureFormset= formset_factory(structureForm, extra = int(numberOfStructures))
    formset = structureFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            if form.cleaned_data['structureType'] == 'Other' or form.cleaned_data['structureType'] == 'none':
                structureType = form.cleaned_data['otherStructure']
            else:
                structureType = form.cleaned_data['structureType']
            numberOfSpecificStructures = form.cleaned_data['numberOfSpecificStructures']
            p = Structure(nurseryName = nurseryName, structureType = structureType, structureAmount = numberOfSpecificStructures, siteObserver = request.session.get('siteObserver'), siteName = siteName)
            p.save()
        return redirect('species')
    else:
        print(formset.errors)
    return render(request, 'dadApp/structure2.html', {'nurseryName' : nurseryName , 'siteName' : siteName , 'message' : message , 'formset' : formset})


def species(request):
    nurseryName = request.session.get('nurseryName')
    siteName = request.session.get('siteName')

    form = numberOfSpeciesForm(request.POST or None)
    if form.is_valid():
        numberOfSpecies = form.cleaned_data['numberOfSpecies']
        request.session['numberOfSpecies'] = numberOfSpecies
        return redirect('specificSpecies')
    else:
        print("fuck that")
    return render(request, 'dadApp/species.html', {'nurseryName' : nurseryName , 'siteName' : siteName , 'form' : form})

def specificSpecies(request):
    nurseryName = request.session.get('nurseryName')
    siteName = request.session.get('siteName')
    numberOfSpecies = request.session.get('numberOfSpecies')
    if int(numberOfSpecies) == 0:
        return redirect('end')
    message = "Please input the " + str(numberOfSpecies) + " Species"
    speciesFormset= formset_factory(speciesForm, extra = int(numberOfSpecies))
    formset = speciesFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            if form.cleaned_data['speciesType'] == 'Other' or form.cleaned_data['speciesType'] == 'none':
                speciesType = form.cleaned_data['otherSpecies']
            else:
                speciesType = form.cleaned_data['speciesType']
            numberOfSmallFragments = form.cleaned_data['numberOfSmallFragments']
            numberOfMediumFragments = form.cleaned_data['numberOfMediumFragments']
            numberOfLargeFragments = form.cleaned_data['numberOfLargeFragments']
            numberOfXLargeFragments = form.cleaned_data['numberOfXLargeFragments']
            numberOfFragments = int(numberOfSmallFragments) + int(numberOfMediumFragments) + int(numberOfLargeFragments) + int(numberOfXLargeFragments)
            numberOfGenets = form.cleaned_data['numberOfGenets']
            percentOfDead = form.cleaned_data['percentOfDead']
            percentOfDiseased = form.cleaned_data['percentOfDiseased']
            percentOfBleached = form.cleaned_data['percentOfBleached']
            percentOfBroken = form.cleaned_data['percentOfBroken']
            p = Species(nurseryName = nurseryName, speciesType = speciesType,
                        speciesSmall=numberOfSmallFragments, speciesMedium = numberOfMediumFragments,
                        speciesLarge = numberOfLargeFragments, speciesXLarge = numberOfXLargeFragments,
                        speciesFragment = numberOfFragments, speciesGenet = numberOfGenets,
                        percent100Dead = percentOfDead, percentOfDiseased = percentOfDiseased,
                        percentOfBleached = percentOfBleached, percentOfBroken = percentOfBroken,
                        siteObserver = request.session.get('siteObserver'))
            p.save()
        return redirect('index')
    else:
        print(formset.errors)
    return render(request, 'dadApp/species2.html', {'nurseryName' : nurseryName , 'siteName' : siteName , 'message' : message , 'formset' : formset})

def collection(request):
    return HttpResponse("COLLECTION SHIT")

def outplant(request):
    return HttpResponse("OUTPLANT SHIT")

def damage(request):
    form = damageForm(request.POST or None)
    return render(request, 'dadApp/damage.html', {'form' : form})

def maintenance(request):
    form = maintenanceForm(request.POST or None)
    return render(request, 'dadApp/maintenance.html', {'form' : form})

def end(request):
    return HttpResponse("YOU HAVE FINSIHED INPUTTING DATA")
