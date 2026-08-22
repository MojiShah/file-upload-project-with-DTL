from django.shortcuts import render
from django.http import HttpRequest

def home_page(request:HttpRequest):
    return render(request=request,template_name='home/index.html',context={})