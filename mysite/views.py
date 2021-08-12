from django.views.generic import TemplateView
from django.db.models.aggregates import Avg
from django.db.models.expressions import F
from review.models import Post
from wine.models import Wine
from purchases.models import Shop

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        wine_top5 = Wine.objects \
                        .annotate(Avg('post__rating')) \
                        .order_by('-post__rating__avg')[:5]
        shop_list = Shop.objects.all()[:5]
        self.extra_context = {
            'wine_top5': wine_top5,
            'shop_list': shop_list
        }
        return super().get(request, *args, **kwargs)
