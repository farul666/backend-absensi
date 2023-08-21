from django.contrib import admin
from .models import *

class kolomdata(admin.ModelAdmin):
    list_display = ['nip','nama','username','mapel','jk','agama','password','alamat']
    search_fields = ['nip','nama']
    list_filter = ('nama',)
    list_per_page = 7

admin.site.register(Biodata,kolomdata)
admin.site.register(Jenis)
admin.site.register(Agama)
