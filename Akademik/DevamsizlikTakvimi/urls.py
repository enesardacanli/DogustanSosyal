from . import views
from django.urls import path


urlpatterns = [
    path('devamsizlikTakvimi/', views.devamsizlikTakvimi),
]