from django.urls import path

# from . import views
from .views import *

app_name = 'chat'

urlpatterns = [
    # path('<str:room_name>/', views.room, name='room'),
    path('<str:room_name>/', RoomView.as_view(), name='room'),
]
