from django.shortcuts import render
from django.views.generic import TemplateView

class globalView(TemplateView):
    template_name = 'country/area.html'

class GlobalListView(TemplateView):
    template_name = 'country/area_list.html'

# Create your views here.
