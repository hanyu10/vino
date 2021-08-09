from django.views.generic import FormView, DetailView
from .models import Shop
from .forms import ShopForm
from django.core.paginator import Paginator

class ShopView(FormView):
    template_name = 'purchases/store.html'
    form_class = ShopForm
    success_url = '.'

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        area = request.GET.get('area')
        shop_list = Shop.objects.all()
        
        if name:
            shop_list = shop_list.filter(name__icontains=name)
        if area:
            shop_list = shop_list.filter(area=area)
       
        paginator = Paginator(shop_list, 5)
        page = request.GET.get('page', 1)
        shop_list = paginator.get_page(page)
        shop_query = []
        if name:
            shop_query.append(f'name={name}')
        if area:
            shop_query.append(f'area={area}')
        

        self.extra_context = {
            'shop_list': shop_list,
            'shop_query': shop_query
        }
        return super().get(request, *args, **kwargs)

class ShopDetailView(DetailView):
    model = Shop
    context_object_name = 'shop'
