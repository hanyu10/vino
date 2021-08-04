from django.views.generic import TemplateView, DetailView, ListView
from wine.models import Country, Wine

class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine/wine_detail.html'
    context_object_name = 'wine'
