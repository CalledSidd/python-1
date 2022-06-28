from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Pro

# Create your views here.
def index(request):
    pros = Pro.objects.all
    return render(request,'index.html',{'cars':pros})

