from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

# app_name = 'accounts' # 이게 없어야 LoginRequiredMixin 적용 시 리디렉션됨

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(redirect_field_name = 'next'), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('register/done', UserCreateDoneView.as_view(), name='register_done'),
]
