from django.shortcuts import render
from django.views.generic import TemplateView

class WikiView(TemplateView):
    template_name = 'wiki/index.html'

# Create your views here.
