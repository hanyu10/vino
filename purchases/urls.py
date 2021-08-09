from django.urls import path
from .views import *

app_name = 'purchases'

urlpatterns = [
    path('/purchases', ShopView.as_view(), name='store')
]