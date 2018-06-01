from django import forms
from .models import Site

class siteForm(forms.Form):


    siteName = forms.ChoiceField(label = 'Site Name', choices = [])
    otherSite =  forms.CharField(label = 'New Site', required = False)
    siteDate = forms.DateTimeField(label = 'Date')
    siteObserver = forms.CharField(label = 'Your Name', max_length = 100)
    siteNursery = forms.ChoiceField(label = 'Nursery Name', choices = [])
    otherNursery = forms.CharField(label = 'New Nursery', required = False)
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
