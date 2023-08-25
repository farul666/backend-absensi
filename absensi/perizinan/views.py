from django.shortcuts import render, redirect
from perizinan.forms import FormPerizinan
from perizinan.models import Perizinan
from django.contrib import messages

def data_izin(request):
    perizinan=Perizinan.objects.all()

    konteks={
        'perizinan':perizinan,
    }
    return render (request,'Perizinan/data_izin.html',konteks)

# Method untuk menambahkan data pada tabel perizinan
def add_izin(request):
    form = FormPerizinan(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormPerizinan()
        konteks = {
            'form' : form,
        }
        return render(request,'Perizinan/add_izin.html',konteks)
    else:
        form=FormPerizinan()
        konteks = {
            'form' : form,
        }
    return render(request,'Perizinan/add_izin.html',konteks)

#Method untuk edit data pada tabel perizinan
def update_izin(request,id_perizinan) :
    perizinan=Perizinan.objects.get(id=id_perizinan)
    if request.POST:
        form = FormPerizinan(request.POST,instance=perizinan)
        if form.is_valid():
            form.save()
            messages.success (request , "Data Berhasil Diubah")
            return redirect('update_izin',id_perizinan=id_perizinan)
    else:
        form=FormPerizinan(instance=perizinan)
        konteks = {
            'form' : form,
            'perizinan':perizinan
        }
    return render(request,'Perizinan/ubah_izin.html',konteks) 


#Method untuk menghapus data pada tabel perizinan
def hapus_izin(request, id_perizinan ):
    perizinan=Perizinan.objects.get(id=id_perizinan )
    perizinan.delete()
    messages.success(request ,"Data telah di hapus ")
    return redirect ('/perizinan')