from django.urls import path, include
from .views import *

app_name = 'wine'

urlpatterns = [
    path('', WineHomeView.as_view(), name='index'),
    path('search/', include('search.urls')),
    path('detail/<int:pk>/', WineDetailView.as_view(), name='detail')
]
