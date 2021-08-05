from django.urls import path
from .views import *

app_name='pairing'

urlpatterns = [
    path('', PairingView.as_view(), name='index')
]
