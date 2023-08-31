from typing import Any
from django.db import models
from datetime import datetime, date
from biodata.models import Biodata

# nama, tanggal awal izin & tangggal akhir izin serta keterangan


class Perizinan(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE,null=True)
    tgl=models.DateTimeField(auto_now=True)
    keterangan=models.CharField(max_length=250)


    def __str__(self):
        return self.nama
    
   

    
        

    
    