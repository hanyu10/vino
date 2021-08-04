from django.views.generic import TemplateView, DetailView
from wine.models import Country, Wine

class WineHomeView(TemplateView):
    # wine:search 로 리디렉션
    template_name = 'wine/index.html'

class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine/wine_detail.html'
    context_object_name = 'wine'
