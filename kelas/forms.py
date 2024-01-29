from django import forms
from .models import Kelas

class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        fields = ['nama_kelas', 'kompetensi_keahlian']
