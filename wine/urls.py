from django.urls import path, include
from django.views.generic import RedirectView
from .views import *

app_name = 'wine'

urlpatterns = [
    path('', RedirectView.as_view(url='search/')),
    path('search/', include('search.urls')),
    path('detail/<int:pk>/', WineDetailView.as_view(), name='detail'),
]
