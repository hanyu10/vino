from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path('<str:room_name>/', RoomView.as_view(), name='room'),
]
