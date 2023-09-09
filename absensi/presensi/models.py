from django.db import models
from biodata.models import Biodata


class Presensi(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE,null=True)
    tgl=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10)


    def __str__(self):
        return str(self.nama)
    


# Create your models here.
