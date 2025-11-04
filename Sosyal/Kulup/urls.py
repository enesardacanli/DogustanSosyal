from . import views
from django.urls import path

urlpatterns = [
    path('kulup/', views.kulup),
]