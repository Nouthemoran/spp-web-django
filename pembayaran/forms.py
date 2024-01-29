from django import forms
from .models import Pembayaran

class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['id_pembayaran', 'id_petugas', 'nisn', 'tgl_bayar', 'bulan_dibayar', 'tahun_dibayar', 'id_spp', 'jumlah_bayar']
