from django import forms
from .models import Siswa

class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = ['nisn', 'nis', 'nama', 'alamat', 'no_telp', 'id_kelas', 'id_spp']
