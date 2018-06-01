from django.shortcuts import render, redirect, reverse
from .forms import siteForm
from django.http import HttpResponseRedirect
from .models import Site

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def siteInput(request):
    form = siteForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['siteName'] == 'Other' or form.cleaned_data['siteName'] == '-------':
            siteName = form.cleaned_data['otherSite']
        else:
            siteName = form.cleaned_data['siteName']
        siteDate = form.cleaned_data['siteDate']
        siteObserver = form.cleaned_data['siteObserver']
# check if he wants a pull down menu for site name
        if form.cleaned_data['siteNursery'] == 'Other' or form.cleaned_data['siteNursery'] == '-------':
            nurseryName = form.cleaned_data['otherNursery']
        else:
            nurseryName = form.cleaned_data['siteNursery']
        p = Site(siteName=siteName, siteDate=siteDate, siteObserver=siteObserver, nurseryName = nurseryName)
        p.save()
        # return reverse('structure', kwargs={'nurseryName': nurseryName})
        # return redirect('structure', nurseryName = nurseryName)
        return redirect('structure')
    else:
        print("UNSUCCESSFUL")
    # for p in Person.objects.raw('SELECT * FROM myapp_person'):
    # x = Person.objects.raw('SELECT * FROM myapp_person')[0]
    return render(request, 'dadApp/site.html', {'form' : form})
    # return HttpResponse("Hello, world. You're at the polls index.")

def structure(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'dadApp/structure.html', {'nurseryName' : nurseryName})
