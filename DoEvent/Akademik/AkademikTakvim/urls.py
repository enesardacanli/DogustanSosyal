from . import views
from django.urls import path


urlpatterns = [
    path('canliAkademikTakvim/', views.canliAkademikTakvim),
]