from django.shortcuts import render
from django.http.response import HttpResponse


def duyurular(request):
  return render(request, "duyurular.html")
def etkinlikler(request):
  return render(request, "etkinlikler.html")
def kulupler(request):
  return render(request, "kulupler.html")
