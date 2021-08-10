from django.urls import path
from test1.views import *
app_name = 'bookmark'
urlpatterns = [
 path('', wineListView.as_view(), name='index'),
 path('<int:pk>/', wineDetailView.as_view(), name='detail'),
]
