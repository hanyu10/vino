from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from wine.models import Wine

food_list = {
    'beef': '소고기',
    'chicken': '닭고기',
    'cheese': '치즈',
    'fish': '생선요리',
    'lamb': '양고기',
    'pasta': '파스타',
    'pork': '돼지고기',
    'sweet dessert': '달콤한 디저트',
}

class PairingMainView(TemplateView):
    template_name = 'pairing/pairing_main.html'


class PairingView_cook(TemplateView):
    template_name = 'pairing/wine_recipe.html'


class PairingView(TemplateView):
    template_name = 'pairing/pairing.html'
    extra_context = { 'food': food_list }


# class PairingView_beef(TemplateView):
#     template_name = 'pairing/pairing_beef.html'


# class PairingView_chicken(TemplateView):
#     template_name = 'pairing/pairing_chicken.html'


# class PairingView_cheese(TemplateView):
#     template_name = 'pairing/pairing_cheese.html'


# class PairingView_fish(TemplateView):
#     template_name = 'pairing/pairing_fish.html'


# class PairingView_lamb(TemplateView):
#     template_name = 'pairing/pairing_lamb.html'


# class PairingView_pasta(TemplateView):
#     template_name = 'pairing/pairing_pasta.html'


# class PairingView_pork(TemplateView):
#     template_name = 'pairing/pairing_pork.html'


# class PairingView_dessert(TemplateView):
#     template_name = 'pairing/pairing_dessert.html'


class PairingListView(ListView):
    template_name = 'pairing/pairing_list.html'
    context_object_name = 'wine_list'

    def get(self, request, *args, **kwargs):
        food = request.GET.get('food')
        self.queryset = Wine.objects.all().filter(food=food)
        food_kor = food_list.get(food)
        
        paginator = Paginator(self.queryset, 5)
        page = request.GET.get('page', 1)
        self.queryset = paginator.get_page(page)
        food_query = ''
        if food:
            food_query =  f'food={food}'
        self.extra_context = {
            'food': food_kor,
            'food_query': food_query
        }
        return super().get(request, *args, **kwargs)
