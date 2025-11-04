from . import views
from django.urls import path


urlpatterns = [
    path('kulupOner/', views.kulupOner),
]