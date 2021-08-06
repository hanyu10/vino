from django.urls import path
from .views import *

app_name='pairing'

urlpatterns = [
    path('', PairingView.as_view(), name='index'),
    # beef 링크
    path('beef/', PairingView_beef.as_view(), name='beef'),
    # chiken 링크
    path('chiken/', PairingView_chiken.as_view(), name='chiken'),

    # cheese 링크
    path('cheese/', PairingView_cheese.as_view(), name='cheese'),

     # fish 링크
    path('fish/', PairingView_fish.as_view(), name='fish'),

    # lamb 링크
    path('fish/', PairingView_lamb.as_view(), name='lamb'),

     # pasta 링크
    path('pasta/', PairingView_pasta.as_view(), name='pasta'),

     # pork 링크
    path('pork/', PairingView_pork.as_view(), name='pork'),

    # dessert 링크
    path('dessert/', PairingView_dessert.as_view(), name='dessert'),
]

