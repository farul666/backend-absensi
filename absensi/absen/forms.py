from django.forms import ModelForm
from absen.models import Absen
from django import forms


class FormAbsen(ModelForm):
    class Meta :
        model= Absen
        fields='__all__'

        widgets = {
            'nama':forms.Select({'class':'form-control'}),
            'status':forms.TextInput({'class':'form-control'}),
        }