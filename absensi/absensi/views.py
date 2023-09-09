from django.shortcuts import render
from absen.models import Absen
from biodata.models import Biodata
from presensi.models import Presensi
from perizinan.models import Perizinan

def index(request):
    jml_absen=Absen.objects.count()
    jml_bio=Biodata.objects.count()
    jml_pre=Presensi.objects.count()
    jml_izin=Perizinan.objects.count()

    konteks={
        'jml_absen':jml_absen,
        'jml_bio':jml_bio,
        'jml_pre':jml_pre,
        'jml_izin':jml_izin
    }
    return render(request,'index.html',konteks)