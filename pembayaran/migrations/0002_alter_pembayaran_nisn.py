# Generated by Django 5.0.1 on 2024-01-10 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembayaran', '0001_initial'),
        ('siswa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembayaran',
            name='nisn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siswa.siswa'),
        ),
    ]
