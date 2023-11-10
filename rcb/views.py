from django.shortcuts import render
from django.http import *
# Create your views here.
def virat(request):
    return render(request,'virat.html')
def abd(request):
    return HttpResponse('<h1>ABD is named as Mr 360 </h1>')