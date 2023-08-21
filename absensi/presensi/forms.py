from django.forms import ModelForm
from presensi.models import Presensi
from django import forms


class FormPresensi(ModelForm):
    class Meta :
        model=Presensi
        fields='__all__'

        widgets = {
            'nip':forms.TextInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            'username':forms.TextInput({'class':'form-control'}),
        }