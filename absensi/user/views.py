from django.shortcuts import render
from presensi.models import *
from absen.models import *
from perizinan.models import *
from presensi.forms import *
from absen.forms import *
from perizinan.forms import *
# Create your views here.



def homeuser(request):
    presensi=Presensi.objects.all()
    biodata=Biodata.objects.all()
    perizinan=Perizinan.objects.all()
    absen=Absen.objects.all()

    konteks={
        'presensi':presensi,
        'biodata':biodata,
        'perizinan':perizinan,
        'absen':absen,
    }
    return render(request,'User/home_user.html',konteks)