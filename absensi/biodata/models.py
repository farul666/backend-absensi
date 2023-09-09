from django.db import models

# NIP, Nama, Username, Mata Pelajaran yang diampu, Jenis kelamin, Alamat, Agama, Password


class Jenis(models.Model):
    nama=models.CharField(max_length=10)
    ket=models.TextField()

    def __str__(self):
        return self.nama
    
class Agama(models.Model):
    agama = models.CharField('Agama', max_length=256)
    ket=models.TextField()

    def __str__(self):
        return self.agama
        

class Biodata(models.Model):
    nip=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    username=models.CharField(max_length=8)
    mapel=models.CharField(max_length=50)
    jk=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
    agama=models.ForeignKey(Agama, on_delete=models.CASCADE,null=True)
    password=models.CharField(max_length=50)
    alamat=models.TextField()

    def __str__(self):
        return str(self.nama)
        