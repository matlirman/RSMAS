from django.shortcuts import render, redirect, reverse
from .forms import siteForm, structureForm, numberOfStructuresForm, numberOfSpeciesForm, speciesForm, maintenanceForm, damageForm, outplantForm, speciesOutplantForm, collectionForm, collectionSpeciesForm
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from .models import Site, Structure, Species, Maintenance, Damage, Outplant, OutplantSpecies, Collection, CollectionSpecies
from math import *



# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'dadApp/index.html')

def siteInput(request):
    formOne = siteForm(request.POST or None)
    if formOne.is_valid():
        request.session['siteObserver'] = formOne.cleaned_data['siteObserver']
        request.session['siteDate'] = str(formOne.cleaned_data['siteDate'])

        if formOne.cleaned_data['typeofReport'] == 'nursery':
            if formOne.cleaned_data['siteName'] == 'Other' or formOne.cleaned_data['siteName'] == 'none':
                siteName = formOne.cleaned_data['otherSite']
            else:
                siteName = formOne.cleaned_data['siteName']
            request.session['siteName'] = siteName
            siteDate = formOne.cleaned_data['siteDate']
            siteObserver = formOne.cleaned_data['siteObserver']
            if formOne.cleaned_data['siteNursery'] == 'Other':
                nurseryName = formOne.cleaned_data['otherNursery']
            else:
                nurseryName = formOne.cleaned_data['siteNursery']
            request.session['nurseryName'] = nurseryName
            p = Site(siteName=siteName, siteDate=siteDate, siteObserver=siteObserver, nurseryName = nurseryName)
            p.save()
            return redirect('structure')

        elif formOne.cleaned_data['typeofReport'] == 'maintenance':
            return redirect('maintenance')
        else:
            return redirect('damage')
    return render(request, 'dadApp/site.html', {'formOne' : formOne})


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
        return HttpResponse("You reported that you saw 0 species so the form was not rendered")
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
    formOne = collectionForm(request.POST or None)
    if formOne.is_valid():
        request.session['collectionObserver'] = formOne.cleaned_data['collectionObserver']
        request.session['collectionDate'] = str(formOne.cleaned_data['collectionDate'])
        request.session['numberOfSpeciesCollected'] = formOne.cleaned_data['numberOfSpeciesCollected']

        if formOne.cleaned_data['collectionSite'] == 'Other':
            collectionSite = formOne.cleaned_data['otherCollectionSite']
        else:
            collectionSite = formOne.cleaned_data['collectionSite']
        request.session['collectionSite'] = collectionSite
        collectionLat = formOne.cleaned_data['collectionLat']
        collectionLong = formOne.cleaned_data['collectionLong']
        collectionObserver = formOne.cleaned_data['collectionObserver']
        collectionDate = formOne.cleaned_data['collectionDate']
        collectionDepth = formOne.cleaned_data['collectionDepth']

        p = Collection(collectionSite = collectionSite, collectionLat = collectionLat,
                    collectionLong = collectionLong, collectionObserver = collectionObserver,
                    collectionDate = collectionDate, collectionDepth = collectionDepth)
        p.save()
        return redirect('collectionSpecies')
    return render(request, 'dadApp/collection.html', {'formOne' : formOne})


def collectionSpecies(request):
    collectionSite = request.session.get('collectionSite')
    collectionDate = request.session.get('collectionDate')
    collectionObserver = request.session.get('collectionObserver')
    numberOfSpeciesCollected = request.session.get('numberOfSpeciesCollected')

    if int(numberOfSpeciesCollected) == 0:
        return HttpResponse("You reported that you collected 0 species so the form was not rendered")
    collectionFormset= formset_factory(collectionSpeciesForm, extra = int(numberOfSpeciesCollected))
    formset = collectionFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            if form.cleaned_data['collectionSpecies'] == 'Other':
                collectionSpecies = form.cleaned_data['otherCollectionSpecies']
            else:
                collectionSpecies = form.cleaned_data['collectionSpecies']
            collectionColonySize = form.cleaned_data['collectionColonySize']
            collectionFragments = form.cleaned_data['collectionFragments']
            collectionTLE = form.cleaned_data['collectionTLE']

            p = CollectionSpecies(collectionSite = collectionSite, collectionDate = collectionDate,
                collectionObserver = collectionObserver, collectionSpecies = collectionSpecies,
                collectionColonySize = collectionColonySize, collectionFragments = collectionFragments,
                collectionTLE = collectionTLE)
            p.save()
        return redirect('index')
    else:
        print(formset.errors)
    return render(request, 'dadApp/outplantSpecies.html', {'numberOfSpeciesCollected' : numberOfSpeciesCollected , 'collectionSite' : collectionSite , 'formset' : formset})


def damage(request):
    form = damageForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['typeOfDamage'] == 'Other':
            typeOfDamage = form.cleaned_data['otherDamage']
        else:
            typeOfDamage = form.cleaned_data['typeOfDamage']
        p = Damage(siteObserver = request.session.get('siteObserver'), siteName = request.session.get('siteName'),
                        nurseryName = request.session.get('nurseryName'), typeOfDamage = typeOfDamage,
                        DamageObservedDate = request.session.get('siteDate'))
        p.save()
        return redirect('index')
    return render(request, 'dadApp/damage.html', {'nurseryName' : request.session.get('nurseryName'), 'form' : form})

def maintenance(request):
    form = maintenanceForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['typeOfMaintenance'] == 'Other':
            typeOfMaintenance = form.cleaned_data['otherMaintenance']
        else:
            typeOfMaintenance = form.cleaned_data['typeOfMaintenance']

        p = Maintenance(siteObserver = request.session.get('siteObserver'), siteName = request.session.get('siteName'),
                        nurseryName = request.session.get('nurseryName'), typeOfMaintenance = typeOfMaintenance,
                        maintenanceDate = request.session.get('siteDate'))
        p.save()
        return redirect('index')
    return render(request, 'dadApp/maintenance.html', {'nurseryName' : request.session.get('nurseryName'), 'form' : form})

def end(request):
    return HttpResponse("YOU HAVE FINSIHED INPUTTING DATA")


def outplant(request):
    formOne = outplantForm(request.POST or None)
    if formOne.is_valid():
        request.session['projectName'] = formOne.cleaned_data['projectName']
        request.session['numberOfSpeciesPlanted'] = formOne.cleaned_data['numberOfSpeciesPlanted']
        request.session['outplantDate'] = str(formOne.cleaned_data['outplantDate'])
        request.session['outplantObserver'] = formOne.cleaned_data['outplantObserver']

        projectName = formOne.cleaned_data['projectName']
        if formOne.cleaned_data['outplantSite'] == 'Other':
            outplantSite = formOne.cleaned_data['otherOutplantSite']
        else:
            outplantSite = formOne.cleaned_data['outplantSite']
        request.session['outplantSite'] = outplantSite
        outplantDate = formOne.cleaned_data['outplantDate']
        outplantObserver = formOne.cleaned_data['outplantObserver']
        outplantLat = formOne.cleaned_data['outplantLat']
        outplantLong = formOne.cleaned_data['outplantLong']
        p = Outplant(projectName = projectName, outplantSite = outplantSite,
                    outplantDate = outplantDate, outplantObserver=outplantObserver,
                    outplantLat = outplantLat, outplantLong = outplantLong)
        p.save()
        return redirect('outplantSpecies')
    return render(request, 'dadApp/outplant.html', {'formOne' : formOne})


def outplantSpecies(request):
    projectName = request.session.get('projectName')
    outplantSite = request.session.get('outplantSite')
    numberOfSpeciesPlanted = request.session.get('numberOfSpeciesPlanted')
    outplantDate = request.session.get('outplantDate')
    outplantObserver = request.session.get('outplantObserver')

    if int(numberOfSpeciesPlanted) == 0:
        return HttpResponse("You reported that you outplanted 0 species so the form was not rendered")
    outplantFormset= formset_factory(speciesOutplantForm, extra = int(numberOfSpeciesPlanted))
    formset = outplantFormset(request.POST or None)
    if formset.is_valid():
        for form in formset:
            if form.cleaned_data['speciesType'] == 'Other':
                speciesType = form.cleaned_data['otherSpecies']
            else:
                speciesType = form.cleaned_data['speciesType']
            numberOfSmallFragments = form.cleaned_data['numberOfSmallFragments']
            numberOfMediumFragments = form.cleaned_data['numberOfMediumFragments']
            numberOfLargeFragments = form.cleaned_data['numberOfLargeFragments']
            numberOfXLargeFragments = form.cleaned_data['numberOfXLargeFragments']
            speciesTotal = int(numberOfSmallFragments) + int(numberOfMediumFragments) + int(numberOfLargeFragments) + int(numberOfXLargeFragments)
            if form.cleaned_data['methodOfOutplant'] == 'Other':
                methodOfOutplant = form.cleaned_data['otherMethodOfOutplant']
            else:
                methodOfOutplant = form.cleaned_data['methodOfOutplant']
            p = OutplantSpecies(projectName = projectName, outplantSite = outplantSite,
                outplantDate = outplantDate, outplantObserver = outplantObserver,
                outplantSpeciesType = speciesType, outplantSpeciesSmall = numberOfSmallFragments,
                outplantSpeciesMedium = numberOfMediumFragments, outplantSpeciesLarge = numberOfLargeFragments,
                outplantSpeciesXLarge = numberOfXLargeFragments, outplantSpeciesTotal = speciesTotal,
                speciesOutplantMethod = methodOfOutplant)
            p.save()
        return redirect('index')
    else:
        print(formset.errors)
    return render(request, 'dadApp/outplantSpecies.html', {'numberOfSpeciesPlanted' : numberOfSpeciesPlanted , 'outplantSite' : outplantSite , 'projectName' : projectName , 'formset' : formset})
