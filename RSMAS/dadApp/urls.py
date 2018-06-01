from django.urls import path

from . import views

urlpatterns = [
    path('', views.siteInput, name='siteInput'),

    path('structure/', views.structure, name= 'structure'),
]
