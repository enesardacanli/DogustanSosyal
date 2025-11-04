from . import views
from django.urls import path


urlpatterns = [
    path('duyurular/', views.duyurular),
    path('etkinlikler/', views.etkinlikler),
    path('kulupler/', views.kulupler),
]