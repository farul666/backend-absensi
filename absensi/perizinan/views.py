# from django.shortcuts import render, redirect
# from perizinan.forms import FormPerizinan
# from perizinan.models import Perizinan
# from django.contrib import messages


# # Method untuk menampilkan data pada app Biodata yang terdapat pada database
# def perizinan(request):
#     perizinan=Perizinan.object.all()

#     konteks={
#         'perizinan':perizinan
#     }
#     return render(request,'Perizinan/data_izin.html',konteks)

# # Method untuk menambahkan data pada tabel biodata
# def tambahizn(request):
#     form = FormPerizinan(request.POST)
#     if form.is_valid():
#         form.save()
#         messages.succes(request,"Data berhasil ditambahkan",)
#         form = FormPerizinan()
#         konteks = {
#             'form' : form,
#         }
#         return render(request,'Biodata/add_bd.html',konteks)
#     else:
#         form=FormPerizinan()
#         konteks = {
#             'form' : form,
#         }
#     return render(request,'Perizinan/add_izin.html',konteks)

# #Method untuk edit data pada tabel biodata
# def ubahdt(request,id_perizinan) :
#     perizinan=Perizinan.obejcts.get(id=id_perizinan)
#     if request.POST:
#         form = FormPerizinan(request.POST,instance=perizinan)
#         if form.is_valid():
#             form.save()
#             messages.success (request , "Data Berhasil Diubah")
#             return redirect('Biodata_Edit',id_perizinan=id_perizinan)
#     else:
#         form=FormPerizinan(instance=perizinan)
#         konteks = {
#             'form' : form,
#             'perizinan':perizinan
#         }
#     return render(request,'Perizinan/ubah_izin.html',konteks) 

# #Method untuk menghapus data pada tabel biodata
# def hapusdt(request, id_perizinan ):
#     perizinan=Perizinan.objects.get(id=id_perizinan )
#     perizinan.delete()
#     messages.success(request ,"Data telah di hapus ")
#     return redirect ('/perizinan')
