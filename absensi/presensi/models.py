from django.db import models
from biodata.models import Biodata
from datetime import datetime


class Presensi(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=10)
    tgl=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.nama)
    


# Create your models here.
