from django.db import models

class SPP(models.Model):
    id_spp = models.IntegerField(primary_key=True)  # id_spp sebagai primary key
    tahun = models.IntegerField()
    nominal = models.IntegerField()
    
    def __str__(self):
        return f"{self.id_spp} - {self.tahun}"
