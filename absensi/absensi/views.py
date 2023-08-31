from django.shortcuts import render, redirect
from django.conf.urls.static import static
from absensi.forms import FormAbsensi
from absensi.models import Absensi
from django.contrib import messages


def index(request):
    return render(request,'index.html')



# Method untuk menampilkan data pada absensi
def data_absensi(request):
    absensi=Absensi.objects.all()

    konteks={
        'absensi':absensi,
    }
    return render(request,'Absensi/data_absensi.html',konteks)

# Method untuk menambahkan data pada tabel absensi
def tambah_absensi(request):
    form = FormAbsensi(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormAbsensi()
        konteks = {
            'form' : form,
        }
        return render(request,'Absensi/add_absensi.html',konteks)
    else:
        form=FormAbsensi()
        konteks = {
            'form' : form,
        }
    return render(request,'Absensi/add_absensi.html',konteks)

#Method untuk edit data pada tabel biodata
def update_absensi(request,id_absensi) :
    absensi=Absensi.objects.get(id=id_absensi)
    if request.POST:
        form = FormAbsensi(request.POST,instance=absensi)
        if form.is_valid():
            form.save()
            messages.success (request , "Data Berhasil Diubah")
            return redirect('update_dt',id_absensi=id_absensi)
    else:
        form=FormAbsensi(instance=absensi)
        konteks = {
            'form' : form,
            'biodatas':absensi
        }
    return render(request,'Absensi/ubah_absensi.html',konteks) 

#Method untuk menghapus data pada tabel biodata
def hapus_absensi(request, id_absensi ):
    absensi=Absensi.objects.get(id=id_absensi )
    absensi.delete()
    messages.success(request ,"Data telah di hapus ")
    return redirect ('/absensi')

