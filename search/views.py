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

        # 검색 결과 전달
        wine_list = Wine.objects.all()
        if name:
            wine_list = wine_list.filter(name__icontains=name) # icontains는 대소문자 구분 안함
        if wine_type:
            wine_list = wine_list.filter(wine_type=wine_type)
        if food:
            wine_list = wine_list.filter(food=food)
        if sugar:
            wine_list = wine_list.filter(sugar=sugar)
        if sour:
            wine_list = wine_list.filter(sour=sour)

        # 페이지네이션
        paginator = Paginator(wine_list, 5)
        page = request.GET.get('page', 1)
        wine_list = paginator.get_page(page)
        wine_query = []
        if name:
            wine_query.append(f'name={name}')
        if wine_type:
            wine_query.append(f'wine_type={wine_type}')
        if food:
            wine_query.append(f'food={food}')
        if sugar:
            wine_query.append(f'sugar={sugar}')
        if sour:
            wine_query.append(f'sour={sour}')
        if wine_query:
            wine_query = '&'.join(wine_query)
        else:
            wine_query = None

        self.extra_context = {
            'wine_list': wine_list,
            'wine_query': wine_query
        }
        return super().get(request, *args, **kwargs)
