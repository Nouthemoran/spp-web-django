from django.db import models

class Siswa(models.Model):
    nisn = models.CharField(max_length=10, primary_key=True)
    nis = models.CharField(max_length=8)
    nama = models.CharField(max_length=35)
    alamat = models.TextField()
    no_telp = models.CharField(max_length=13)
    
    # Ubah ini menjadi ForeignKey dengan string
    id_kelas = models.ForeignKey('kelas.Kelas', on_delete=models.CASCADE)
    id_spp = models.ForeignKey('spp.SPP', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nisn} - {self.nama}"
