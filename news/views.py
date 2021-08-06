from django.views.generic import TemplateView
from django.core.paginator import Paginator
from news.naver_news import get_news_json

class NewsView(TemplateView):
    template_name = 'news/index.html'
    
    def get(self, request, *args, **kwargs):
        news = get_news_json('와인', 1, 100)
        paginator = Paginator(news, 10)
        page = request.GET.get('page', 1)
        news = paginator.get_page(page)
        self.extra_context = {'news': news}
        return super().get(request, *args, **kwargs)
