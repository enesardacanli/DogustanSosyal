from django.shortcuts import render
from django.http.response import HttpResponse




def randevuSistemi(request):
  return render(request,"randevuSistemi.html")
