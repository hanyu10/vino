from django.views.generic import FormView, DetailView
from .models import Shop
from .forms import ShopForm
from django.core.paginator import Paginator

class ShopView(FormView):
    template_name = 'purchases/store.html'
    form_class = ShopForm
    success_url = '.'

    def get(self, request, *args, **kwargs):
        shop_name = request.GET.get('shop_name')
        shop_area = request.GET.get('shop_area')
        shop_list = Shop.objects.all()
        
        if shop_name:
            shop_list = shop_list.filter(name__icontains=shop_name)
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

class ShopDetailView(DetailView):
    model = Shop
    context_object_name = 'shop'
