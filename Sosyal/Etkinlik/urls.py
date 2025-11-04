from . import views
from django.urls import path


urlpatterns = [
    path('etkinlik/', views.etkinlik),
]