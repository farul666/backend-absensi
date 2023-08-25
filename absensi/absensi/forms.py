from django.forms import ModelForm
from absensi.models import Absensi
from django import forms


class FormAbsensi(ModelForm):
    class Meta :
        model= Absensi
        fields='__all__'

        widgets = {
            'nama':forms.TextInput({'class':'form-control'}),
            'keterangan':forms.TextInput({'class':'form-control'}),
        }