from django.views.generic import TemplateView

class WineView(TemplateView):
    template_name = 'wine/index.html'
