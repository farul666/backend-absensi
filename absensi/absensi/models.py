from typing import Any
from django.db import models
from datetime import datetime, date

# nama, tanggal awal izin & tangggal akhir izin serta keterangan


class Absensi(models.Model):
    nama=models.CharField(max_length=50)
    tgl=models.DateTimeField(auto_now_add=True)
    keterangan=models.CharField(max_length=250)


    def __str__(self):
        return self.nama
    
   

    
        

    
    