from django.urls import path
from .views import *

app_name = 'country'

urlpatterns = [
    path('', globalView.as_view(), name='index')
]