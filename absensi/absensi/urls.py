"""
URL configuration for absensi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    # Route untuk Biodata
    path('admin/', admin.site.urls),
    path('', views.index),

    # CRUD Biodata
    path('biodata/', views.data),
    # path('tambahbd/',views.tambahdt),
    # path('ubahdt/',views.ubahdt),
    # path('hapusdt/',views.hapusdt),

    # CRUD Perizinan
    path('perizinan/',views.perizinan),
    # path('tambahizn/',views.tambahizin),
    # path('ubahizn/',views.ubahizin),
    # path('hapusizn/',views.hapusizin),

    # CRUD Laporan
    path('laporan/',views.laporan),
    # path('cetaklpr',views.cetaklpr),
    

]
