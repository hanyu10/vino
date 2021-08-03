from django.urls import path, include
from .views import *

app_name = 'wine'

urlpatterns = [
    path('', WineView.as_view(), name='index'),
    path('search/', include('search.urls')),
]
