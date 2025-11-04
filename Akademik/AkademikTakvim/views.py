from django.shortcuts import render
from django.http.response import HttpResponse


def canliAkademikTakvim(request):
  return render(request, "canliAkademikTakvim.html")

