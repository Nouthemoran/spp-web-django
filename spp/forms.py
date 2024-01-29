from django import forms
from .models import SPP

class SPPForm(forms.ModelForm):
    class Meta:
        model = SPP
        fields = ['tahun', 'nominal']
