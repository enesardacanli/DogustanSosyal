from . import views
from django.urls import path


urlpatterns = [
    path('etkinlikOner/', views.etkinlikOner),
]