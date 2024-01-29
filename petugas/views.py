from django.shortcuts import render, redirect, get_object_or_404
from .models import Petugas
from .forms import PetugasForm

def daftar_petugas(request):
    petugas_list = Petugas.objects.all()  
    return render(request, 'petugas/daftar_petugas.html', {'petugas_list': petugas_list})

def tambah_petugas(request):
    if request.method == 'POST':
        form = PetugasForm(request.POST)
        if form.is_valid():
            # Mendapatkan nilai id_petugas dari form atau request
            id_petugas = request.POST.get('id_petugas')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            nama_petugas = form.cleaned_data['nama_petugas']
            level = form.cleaned_data['level']
            
            # Membuat objek Petugas dengan id_petugas yang diberikan
            petugas = Petugas(id_petugas=id_petugas, username=username, password=password, nama_petugas=nama_petugas, level=level)
            petugas.save()
            return redirect('petugas:daftar_petugas')
    else:
        form = PetugasForm()
    
    return render(request, 'petugas/tambah_petugas.html', {'form': form})


def detail_petugas(request, petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)  
    return render(request, 'petugas/detail_petugas.html', {'petugas': petugas})

def edit_petugas(request, petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)
    if request.method == 'POST':
        form = PetugasForm(request.POST, instance=petugas)
        if form.is_valid():
            form.save()
            return redirect('petugas:daftar_petugas')
    else:
        form = PetugasForm(instance=petugas)
    return render(request, 'petugas/edit_petugas.html', {'form': form, 'petugas': petugas})

def hapus_petugas(request, petugas_id):
    petugas = get_object_or_404(Petugas, pk=petugas_id)
    petugas.delete()
    return redirect('petugas:daftar_petugas')
