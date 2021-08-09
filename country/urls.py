from django.urls import path
from .views import *
from django.urls import path

from . import views

app_name = 'country'

urlpatterns = [
    path('', globalView.as_view(), name='index'),
    path('france/', FranceListView.as_view(), name='france'),
    path('spain/', SpainListView.as_view(), name='spain'),
    path('italy/', ItalyListView.as_view(), name='italy'),
    path('portugal/', PortugalListView.as_view(), name='portugal'),
]
