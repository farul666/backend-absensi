from django.shortcuts import render
from django.conf.urls.static import static

def index(request):
    return render(request,'index.html')

def data(request):
    return render(request,'biodata.html')

def perizinan(request):
    return render(request,'perizinan.html')