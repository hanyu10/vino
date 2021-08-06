from django.db.models import query
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from search.forms import SearchForm
from wine.models import Wine
from django.core.paginator import Paginator





class SearchView(FormView):
    template_name = 'search/index.html'
    form_class = SearchForm
    success_url = '.'
    
    

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        wine_type = request.GET.get('wine_type')
        food = request.GET.get('food')
        sugar = request.GET.get('sugar')
        sour = request.GET.get('sour')
        # print(f"GET 요청의 파라미터 : ({name}, {wine_type}, {food}, {sugar}, {sour})")
        page=request.GET.get('page', 1)
        wine_list = Wine.objects.all()
        
        if name:
            wine_list = wine_list.filter(name__contains=name)
        if wine_type:
            wine_list = wine_list.filter(wine_type=wine_type)
        if food:
            wine_list = wine_list.filter(food=food)
        if sugar:
            wine_list = wine_list.filter(sugar=sugar)
        if sour:
            wine_list = wine_list.filter(sour=sour)

        
        paginator = Paginator(wine_list, 5)
        wine_list=paginator.get_page(page)
        
        

        # print(wine_list)
        self.extra_context = {'wine_list': wine_list}
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        wine_type = request.POST.get('wine_type')
        food = request.POST.get('food')
        sugar = request.POST.get('sugar')
        sour = request.POST.get('sour')
        # print(f"POST 요청의 form 파라미터 : ({name}, {wine_type}, {food}, {sugar}, {sour})")
        self.success_url = f'./'
        wine_query = []
        if (name):
            wine_query.append(f'name={name}')
        if (wine_type):
            wine_query.append(f'wine_type={wine_type}')
        if (food):
            wine_query.append(f'food={food}')
        if (sugar):
            wine_query.append(f'sugar={sugar}')
        if (sour):
            wine_query.append(f'sour={sour}')
        if wine_query:
            self.success_url += '?' + '&'.join(wine_query)
        return super().post(request, *args, **kwargs)