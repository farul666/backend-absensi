from django.shortcuts import render, redirect
from presensi.forms import FormPresensi
from presensi.models import Presensi
from django.contrib import messages
from biodata.models import Biodata

# method untuk menampilkan data pada app presensi
def presensi(request):
    presensi=Presensi.objects.all()
    biodata=Biodata.objects.all()

    konteks={
        'presensi':presensi,
        'biodata':biodata,
    }
    return render(request,'Presensi/data_presensi.html',konteks)

# method untuk menampilkan data pada taebel presensi
def tambahpresensi(request):
    form=FormPresensi(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormPresensi()
        konteks ={
            'form': form
        }
        return render(request,'Presensi/add_presensi.html',konteks)
    else:
        form=FormPresensi()
        konteks={
            'form':form
        }
    return render(request,'Presensi/add_presensi.html',konteks)

# method untuk edit data pada app presensi
def update_pre(request,id_presensi):
    presensi=Presensi.objects.get(id=id_presensi)
    if request.POST:
        form = FormPresensi(request.POST,instance=presensi)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect('update_pre',id_presensi=id_presensi)
        else:
            form=FormPresensi(instance=presensi)
            konteks ={
                'form' :form,
                'presensi' :presensi
            }
        return render(request,'Presensi/ubah_presensi.html',konteks)
    

# method untuk menghapusn data pada app presensi
def hapuspresensi(request,id_presensi):
    presensi =Presensi.objects.get(id=id_presensi)
    presensi.delete()
    messages.success(request,"Data berhasil dihapus")
    return redirect ('/presensi')
        


# Create your views here.
