from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'kzauth'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reg/', views.RegUser.as_view(), name='reg')
]