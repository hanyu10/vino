from django.shortcuts import render
from django.db.models import query
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from search.forms import SearchForm
from wine.models import Shop
from django.core.paginator import Paginator

class ShopView(FormView):
    template_name = 'purchases/store.html'
    form_class = SearchForm
    success_url = '.'

    def get(self, request, *args, **kwargs):
        shop_name = request.GET.get('shop_name')
        shop_area = request.GET.get('shop_area')
        shop_list = Shop.objects.all()
        
        if shop_name:
            shop_list = shop_list.filter(name__contains=shop_name)
        if shop_area:
            shop_list = shop_list.filter(area=shop_area)
       

        paginator = Paginator(shop_list, 5)
        page = request.GET.get('page', 1)
        shop_list = paginator.get_page(page)
        shop_query = []
        if shop_name:
            shop_query.append(f'name={shop_name}')
        if shop_area:
            shop_query.append(f'wine_type={shop_area}')
        

        self.extra_context = {
            'shop_list': shop_list,
            'shop_query': shop_query
        }
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        shop_name = request.POST.get('shop_name')
        shop_area = request.POST.get('shop_area')
        shop_address = request.POST.get('shop_address')
       
     
        self.success_url = f'./'
        shop_query = []
        if shop_name:
            shop_query.append(f'shop_name={shop_name}')
        if shop_area:
            shop_query.append(f'shop_area={shop_area}')
        if shop_address:
            shop_query.append(f'shop_address={shop_address}')
     
        if shop_query:
            self.success_url += '?' + '&'.join(shop_query)
        return super().post(request, *args, **kwargs)



