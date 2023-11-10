from django.shortcuts import render
from django.http import *
# Create your views here.
def rohith(request):
    return render(request,'rohith.html')
def sky(request):
    return HttpResponse('<h1>SKY is Number one Batsmen in T20 </h1>')