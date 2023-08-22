from django.db import models
from biodata.models import Biodata

# NIP,nama,status,Waktu,tanggal

class Status(models.Model):
    status = models.CharField(max_length=20)
    ket=models.TextField()

    def __str__(self):
        return self.status
        


class Presensi(models.Model):
    nip=models.CharField(max_length=20)
    nama=models.CharField(max_length=50)
    waktu=models.TimeField()
    tanggal=models.DateField()
    status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.nama
    


# Create your models here.
