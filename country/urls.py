from django.urls import path
from .views import *

from . import views

app_name = 'country'

urlpatterns = [
    path('', CountryMainView.as_view(), name='main'),
    path('index/', CountryView.as_view(), name='index'),
    path('list/', CountryListView.as_view(), name='list'),
    # path('', globalView.as_view(), name='index'),
    # path('france/', FranceListView.as_view(), name='france'),
    # path('spain/', SpainListView.as_view(), name='spain'),
    # path('italy/', ItalyListView.as_view(), name='italy'),
    # path('portugal/', PortugalListView.as_view(), name='portugal'),
]
