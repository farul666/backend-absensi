from django.shortcuts import render, redirect
from biodata.forms import FormBiodata
from biodata.models import Biodata
from django.contrib import messages


# Method untuk menampilkan data pada app Biodata yang terdapat pada database
def Biodata_View(request):
    biodata=Biodata.object.all()

    konteks={
        'biodata':biodata,
    }
    return render(request,'Biodata/data_bd.html',konteks)

# Method untuk menambahkan data pada tabel biodata
def Biodata_Add(request):
    form = FormBiodata(request.POST)
    if form.is_valid():
        form.save()
        messages.succes(request,"Data berhasil ditambahkan",)
        form = FormBiodata()
        konteks = {
            'form' : form,
        }
        return render(request,'Biodata/add_bd.html',konteks)
    else:
        form=FormBiodata()
        konteks = {
            'form' : form,
        }
    return render(request,'Biodata/add_bd.html',konteks)

#Method untuk edit data pada tabel biodata
def Biodata_Edit(request,id_biodata) :
    biodatas=Biodata.obejcts.get(id=id_biodata)
    if request.POST:
        form = FormBiodata(request.POST,instance=biodatas)
        if form.is_valid():
            form.save()
            messages.success (request , "Data Berhasil Diubah")
            return redirect('Biodata_Edit',id_biodata=id_biodata)
    else:
        form=FormBiodata(instance=biodatas)
        konteks = {
            'form' : form,
            'biodatas':biodatas
        }
    return render(request,'Biodata/ubad_bd.html',konteks) 

#Method untuk menghapus data pada tabel biodata
def Biodata_Delete(request, id_biodata ):
    biodatas=Biodata.objects.get(id=id_biodata )
    biodatas.delete()
    messages.success(request ,"Data telah di hapus ")
    return redirect ('Biodata')