from django.views.generic import TemplateView, DetailView, ListView
from wine.models import Country, Wine
from review.models import Post

class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine/wine_detail.html'
    context_object_name = 'wine'

    def get(self, request, *args, **kwargs):
        review_list = Post.objects.all().filter(wine=self.get_object())
        average_rating = 0
        for review in review_list:
            average_rating += review.rating
        average_rating /= len(review_list)
        self.extra_context = {
            'review_list': review_list,
            'average_rating': average_rating,
        }
        return super().get(request, *args, **kwargs)
