from django.shortcuts import render
from django.conf.urls.static import static

def index(request):
    return render(request,'index.html')

def data(request):
    return render(request,'Biodata/data_bd.html')

def perizinan(request):
    return render(request,'perizinan.html')

def laporan(request):
    return render(request,'laporan.html')