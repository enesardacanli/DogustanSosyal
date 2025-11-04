from django.shortcuts import render
from django.http.response import HttpResponse

def kulupOner(request):
    return render(request, "kulupOner.html")
# Create your views here.
