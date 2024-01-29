# history_pembayaran/models.py
from django.db import models
from pembayaran.models import Pembayaran

class HistoryPembayaran(models.Model):
    pembayaran = models.ForeignKey(Pembayaran, on_delete=models.CASCADE)
    tanggal_bayar = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Riwayat Pembayaran {self.pembayaran} pada {self.tanggal_bayar}'
