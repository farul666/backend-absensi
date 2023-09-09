from django.db import models
from biodata.models import Biodata

# nama, tanggal awal izin & tangggal akhir izin serta keterangan


class Absensii(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE,null=True)
    tgl=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10)


    def __str__(self):
        return self.nama
    
   

    
        

    
    