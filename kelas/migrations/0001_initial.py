# Generated by Django 3.2.16 on 2023-11-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id_kelas', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_kelas', models.CharField(max_length=10)),
                ('kompetensi_keahlian', models.CharField(max_length=50)),
            ],
        ),
    ]
