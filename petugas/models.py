from django.db import models

class Petugas(models.Model):
    id_petugas = models.IntegerField(primary_key=True)  # id_petugas sebagai primary key
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    nama_petugas = models.CharField(max_length=35)
    LEVEL_CHOICES = [
        ('admin', 'Admin'),
        ('petugas', 'Petugas')
    ]
    level = models.CharField(max_length=7, choices=LEVEL_CHOICES)
    
    def __str__(self):
        return f"{self.id_petugas} - {self.nama_petugas}"
