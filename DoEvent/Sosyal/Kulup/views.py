from django.shortcuts import render
from django.http.response import HttpResponse

def kulup(request):
    return render(request, "kulup.html")
