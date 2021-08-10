from django.shortcuts import render
from django.views.generic import ListView, DetailView
from wine.models import Wine, Country

class wineListView(ListView):
 model = Wine
 
class wineDetailView(DetailView):
 model = Wine

# Create your views here.
