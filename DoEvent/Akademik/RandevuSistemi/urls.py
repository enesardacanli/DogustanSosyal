from . import views
from django.urls import path


urlpatterns = [
    path('randevuSistemi/', views.randevuSistemi),
]