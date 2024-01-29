
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from .models import Pembayaran
from .forms import PembayaranForm
from history_pembayaran.models import HistoryPembayaran  # Import model HistoryPembayaran
from django.views import View
from reportlab.pdfgen import canvas


def daftar_pembayaran(request):
    pembayaran_list = Pembayaran.objects.all()
    return render(request, 'pembayaran/daftar_pembayaran.html', {'pembayaran_list': pembayaran_list})

def tambah_pembayaran(request):
    if request.method == 'POST':
        form = PembayaranForm(request.POST)
        if form.is_valid():
            pembayaran = form.save(commit=False)
            bulan_dibayar = int(pembayaran.bulan_dibayar)
            biaya_per_bulan = pembayaran.id_spp.nominal
            total_pembayaran = bulan_dibayar * biaya_per_bulan
            pembayaran.jumlah_bayar = total_pembayaran
            pembayaran.save()

            # Tambahkan entri ke HistoryPembayaran
            HistoryPembayaran.objects.create(pembayaran=pembayaran)

            # Tambahkan notifikasi menggunakan Django messages framework
            messages.success(request, 'Pembayaran berhasil ditambahkan.')

            return redirect('pembayaran:daftar_pembayaran')
    else:
        form = PembayaranForm()

    return render(request, 'pembayaran/tambah_pembayaran.html', {'form': form})

def detail_pembayaran(request, pembayaran_id):
    pembayaran = get_object_or_404(Pembayaran, pk=pembayaran_id)
    return render(request, 'pembayaran/detail_pembayaran.html', {'pembayaran': pembayaran})

def edit_pembayaran(request, pembayaran_id):
    pembayaran = get_object_or_404(Pembayaran, pk=pembayaran_id)
    if request.method == 'POST':
        form = PembayaranForm(request.POST, instance=pembayaran)
        if form.is_valid():
            form.save()
            return redirect('pembayaran:daftar_pembayaran')
    else:
        form = PembayaranForm(instance=pembayaran)
    
    return render(request, 'pembayaran/edit_pembayaran.html', {'form': form, 'pembayaran': pembayaran})

def hapus_pembayaran(request, pembayaran_id):
    pembayaran = get_object_or_404(Pembayaran, pk=pembayaran_id)
    pembayaran.delete()
    return redirect('pembayaran:daftar_pembayaran')

def cetak_pembayaran(request, pembayaran_id):
    pembayaran = Pembayaran.objects.get(id_pembayaran=pembayaran_id)
    template_path = 'pembayaran/cetak_pembayaran.html'
    context = {'pembayaran': pembayaran}
    # Render template
    template = get_template(template_path)
    html = template.render(context)
    # Create PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="bukti_pembayaran.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response