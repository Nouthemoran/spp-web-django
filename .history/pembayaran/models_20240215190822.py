from django.db import models

class Pembayaran(models.Model):
    BULAN_CHOICES = (
        ('1', 'Januari'),
        ('2', 'Februari'),
        ('3', 'Maret'),
        ('4', 'April'),
        ('5', 'Mei'),
        ('6', 'Juni'),
        ('7', 'Juli'),
        ('8', 'Agustus'),
        ('9', 'September'),
        ('10', 'Oktober'),
        ('11', 'November'),
        ('12', 'Desember'),
    )

    id_pembayaran = models.IntegerField(primary_key=True)
    id_petugas = models.ForeignKey('petugas.Petugas', on_delete=models.CASCADE)
    nisn = models.ForeignKey('siswa.Siswa', on_delete=models.CASCADE)
    tgl_bayar = models.IntegerField()
    bulan_dibayar = models.CharField(max_length=2, choices=BULAN_CHOICES)
    tahun_dibayar = models.CharField(max_length=4)
    id_spp = models.ForeignKey('spp.SPP', on_delete=models.CASCADE)
    jumlah_bayar = models.IntegerField()

