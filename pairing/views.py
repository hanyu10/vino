from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PairingView(TemplateView):
    template_name= 'pairing/pairing.html'
    