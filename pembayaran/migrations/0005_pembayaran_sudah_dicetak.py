# Generated by Django 5.0.1 on 2024-01-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembayaran', '0004_alter_pembayaran_id_pembayaran'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembayaran',
            name='sudah_dicetak',
            field=models.BooleanField(default=False),
        ),
    ]
