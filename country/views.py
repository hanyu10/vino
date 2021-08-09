from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from wine.models import Wine, Country


class globalView(TemplateView):
    template_name = 'country/area.html'

class FranceListView(TemplateView):
    template_name = 'country/france_list.html'

class SpainListView(TemplateView):
    template_name = 'country/spain_list.html'

class ItalyListView(TemplateView):
    template_name = 'country/italy_list.html'

class PortugalListView(TemplateView):
    template_name = 'country/portugal_list.html'




# Create your views here.
