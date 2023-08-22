from django.db import models

# nama, tanggal awal izin & tangggal akhir izin serta keterangan


class Perizinan(models.Model):
    nama=models.CharField(max_length=50)
    tglawal=models.DateField(auto_now_add=True)
    tglakhir=models.DateField()
    keterangan=models.CharField(max_length=250)


    def __str__(self):
        return self.nama
    
        

    
    