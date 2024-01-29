# Di views.py
from django.shortcuts import render
from .models import HistoryPembayaran

def history_pembayaran(request):
    # Ambil semua entri dari model HistoryPembayaran
    history_list = HistoryPembayaran.objects.all()

    # Log data ke konsol atau file
    for history in history_list:
        print(history.pembayaran.id_pembayaran, history.tanggal_bayar)

    # Kirim data ke template
    return render(request, 'history_pembayaran/history_pembayaran.html', {'history_list': history_list})
