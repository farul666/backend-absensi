from django.db import models
from biodata.models import Biodata
from datetime import datetime

# nama, tanggal awal izin & tangggal akhir izin serta keterangan


class Absen(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE,null=True)
    tgl=models.DateTimeField(default=datetime.now, blank=True)
    status=models.CharField(max_length=15)


    def __str__(self):
        return self.nama.nip
    
    
    