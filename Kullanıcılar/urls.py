from django.urls import path
from . import views

app_name = 'kullanicilar'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('api/register/', views.register_api, name='register_api'),
]
