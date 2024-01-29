from django.shortcuts import render, redirect, get_object_or_404
from .models import Kelas
from .forms import KelasForm

def daftar_kelas(request):
    kelas_list = Kelas.objects.all()
    return render(request, 'kelas/daftar_kelas.html', {'kelas_list': kelas_list})

def tambah_kelas(request):
    if request.method == 'POST':
        form = KelasForm(request.POST)
        if form.is_valid():
            # Mendapatkan nilai id_kelas dari form atau request
            id_kelas = request.POST.get('id_kelas')
            nama_kelas = form.cleaned_data['nama_kelas']
            kompetensi_keahlian = form.cleaned_data['kompetensi_keahlian']
            
            # Membuat objek Kelas dengan id_kelas yang diberikan
            kelas = Kelas(id_kelas=id_kelas, nama_kelas=nama_kelas, kompetensi_keahlian=kompetensi_keahlian)
            kelas.save()
            return redirect('kelas:daftar_kelas')
    else:
        form = KelasForm()
    
    return render(request, 'kelas/tambah_kelas.html', {'form': form})


def detail_kelas(request, kelas_id):
    kelas = get_object_or_404(Kelas, pk=kelas_id)
    return render(request, 'kelas/detail_kelas.html', {'kelas': kelas})

def edit_kelas(request, kelas_id):
    kelas = get_object_or_404(Kelas, pk=kelas_id)
    if request.method == 'POST':
        form = KelasForm(request.POST, instance=kelas)
        if form.is_valid():
            form.save()
            return redirect('kelas:daftar_kelas')
    else:
        form = KelasForm(instance=kelas)
    return render(request, 'kelas/edit_kelas.html', {'form': form, 'kelas': kelas})

def hapus_kelas(request, kelas_id):
    kelas = get_object_or_404(Kelas, pk=kelas_id)
    kelas.delete()
    return redirect('kelas:daftar_kelas')
