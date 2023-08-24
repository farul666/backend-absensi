from django.shortcuts import render, redirect
from perizinan.forms import FormPerizinan
from perizinan.models import Perizinan
from django.contrib import messages

def data_izin(request):
    perizinan=Perizinan.object.all()

    konteks={
        'perizinan':perizinan,
    }
    return render (request,'Perizinan/index.html',konteks)

# Method untuk menambahkan data
# def tambah_izin(request):
#     form = FormPerizinan(request.POST)
#     if form.is_valid():
#         form.save()
#         messages.success(request,"Data berhasil ditambahkan")
#         form = FormPerizinan()
#         konteks={
#             'form' : form
#         }
#     else:
#         form=FormPerizinan()
#         konteks = {
#             'form' : form,
#         }
#     return render(request,'Perizinan/add_izin.html',konteks)