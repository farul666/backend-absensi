from django.forms import ModelForm
from perizinan.models import Perizinan
from django import forms


class FormPerizinan(ModelForm):
    class Meta :
        model=Perizinan
        fields='__all__'

        widgets = {
            'nip':forms.TextInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            # 'tglawal':forms.DateField({'class':'form-control'}),
            'tglakhir':forms.DateInput({'class':'form-control'}),
            'keterangan':forms.TextInput({'class':'form-control'}),
        }