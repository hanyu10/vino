from django.urls import path
from .views import *

app_name='pairing'

urlpatterns = [
    path('', PairingMainView.as_view(), name='main'),
    path('index/', PairingView.as_view(), name='index'),
    path('cook/', PairingView_cook.as_view(), name='cook'),
    # path('beef/', PairingView_beef.as_view(), name='beef'),
    # path('chicken/', PairingView_chicken.as_view(), name='chicken'),
    # path('cheese/', PairingView_cheese.as_view(), name='cheese'),
    # path('fish/', PairingView_fish.as_view(), name='fish'),
    # path('lamb/', PairingView_lamb.as_view(), name='lamb'),
    # path('pasta/', PairingView_pasta.as_view(), name='pasta'),
    # path('pork/', PairingView_pork.as_view(), name='pork'),
    # path('dessert/', PairingView_dessert.as_view(), name='dessert'),
    # 음식에 어울리는 와인
    path('list/', PairingListView.as_view(), name='list'),
]
