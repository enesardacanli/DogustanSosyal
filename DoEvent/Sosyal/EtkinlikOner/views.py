from django.shortcuts import render
from django.http.response import HttpResponse

def etkinlikOner(request):
    return render(request, "etkinlikOner.html") 
