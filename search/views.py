from django.views.generic import FormView
from search.forms import SearchForm

class SearchView(FormView):
    template_name = 'search/index.html'
    form_class = SearchForm
    success_url = '.'

    def post(self, request, *args, **kwargs):
        # db 조회
        return super().post(request, *args, **kwargs)
