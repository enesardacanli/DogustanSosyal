from django.shortcuts import render
from django.http.response import HttpResponse

def devamsizlikTakvimi(request):
  return render(request,"devamsizlikTakvimi.html")