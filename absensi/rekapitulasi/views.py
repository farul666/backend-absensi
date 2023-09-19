from django.shortcuts import render
from rekapitulasi.models import Rekap

def rekap_data(request):
    rekap=Rekap.objects.filter(rekap__id=1).count()
    
    konteks={
        'rekap':rekap,
    }

    return render(request,'rekap.html',konteks)
