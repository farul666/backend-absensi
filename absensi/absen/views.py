from django.shortcuts import render, redirect
from absen.forms import FormAbsen
from absen.models import Absen
from django.contrib import messages

# Method untuk menampilkan data pada absensi
def data_absensi(request):
    absen=Absen.objects.all()
    konteks={
        'absen':absen,
    }
    return render(request,'Absensi/data_absensi.html',konteks)

# Method untuk menambahkan data pada tabel absensi
def tambah_absensi(request):
    form = FormAbsen(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormAbsen()
        konteks = {
            'form' : form,
        }
        return render(request,'Absensi/add_absensi.html',konteks)
    else:
        form=FormAbsen()
        konteks = {
            'form' : form,
        }
    return render(request,'Absensi/add_absensi.html',konteks)

#Method untuk menghapus data pada tabel biodata
def hapus_absensi(request, id_absen ):
    absensi=Absen.objects.get(id=id_absen )
    absensi.delete()
    messages.success(request ,"Data telah di hapus ")
    return redirect ('/absensi')

