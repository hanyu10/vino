# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.views.generic import ListView, DetailView
# from django.views.generic import FormView
# from wine.models import Wine, Country

from django.views.generic import TemplateView, ListView
from wine.models import Wine

country_list = {
    'portugal': '포르투칼',
    'france' : '프랑스',
    'spain' : '스페인',
    'italy' : '이탈리아',
    'germany' : '독일',
    'austria' : '오스트리아'    
}

class CountryMainView(TemplateView):
    template_name = 'country/country_main.html'

class CountryView(TemplateView):
    template_name = 'country/country.html'
    extra_context = { 'area': country_list }

class CountryListView(ListView):
    template_name = 'country/country_list.html'
    context_object_name = 'wine_list'

    def get(self, request, *args, **kwargs):
        country = request.GET.get('area')
        self.queryset = Wine.objects.all().filter(area__area=country)
        food_kor = country_list.get(country)
        self.extra_context = { 'area': food_kor }
        return super().get(request, *args, **kwargs)

# class globalView(TemplateView):
#     template_name = 'country/area.html'

# class FranceListView(TemplateView):
#     template_name = 'country/france_list.html'

# class SpainListView(TemplateView):
#     template_name = 'country/spain_list.html'

# class ItalyListView(TemplateView):
#     template_name = 'country/italy_list.html'

# class PortugalListView(TemplateView):
#     template_name = 'country/portugal_list.html'




# Create your views here.
