from django.shortcuts import render
from django.http.response import HttpResponse


def etkinlik(request):
  return render(request, "etkinlik.html")