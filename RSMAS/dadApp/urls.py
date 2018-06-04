from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('siteInput/', views.siteInput, name = 'siteInput'),

    path('structure/', views.structure, name= 'structure'),

    path('specificStructure/', views.specificStructure, name = 'specificStructure'),

    path('species/', views.species, name = 'species'),

    path('specificSpecies/', views.specificSpecies, name = 'specificSpecies'),

    path('collection/', views.collection, name = 'collection'),

    path('collectionSpecies/', views.collectionSpecies, name = 'collectionSpecies'),

    path('outplant/', views.outplant, name = 'outplant'),

    path('outplantSpecies/', views.outplantSpecies, name = 'outplantSpecies'),

    path('maintenance/', views.maintenance, name = 'maintenance'),

    path('damage/', views.damage, name = 'damage'),

    path('end', views.end, name = 'end'),
]
