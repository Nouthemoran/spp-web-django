from django.db import models

class Kelas(models.Model):
    id_kelas = models.IntegerField(primary_key=True)  # id_kelas sebagai primary key
    nama_kelas = models.CharField(max_length=10)
    kompetensi_keahlian = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nama_kelas} - {self.kompetensi_keahlian}"