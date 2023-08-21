from django.db import models

# NIP, Nama, Username, Mata Pelajaran yang diampu, Jenis kelamin, Alamat, Agama, Password


class Perizinan(models.Model):
    nama=models.CharField(max_length=50)
    tglawal=models.DateField()
    tglakhir=models.DateField()
    keterangan=models.CharField(max_length=250)


    def __str__(self):
        return self.nama
    
        

    
    