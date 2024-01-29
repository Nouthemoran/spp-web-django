from django.shortcuts import render, redirect, get_object_or_404
from .models import Siswa
from .forms import SiswaForm

def daftar_siswa(request):
    siswa_list = Siswa.objects.all()
    return render(request, 'siswa/daftar_siswa.html', {'siswa_list': siswa_list})

def tambah_siswa(request):
    if request.method == 'POST':
        form = SiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('siswa:daftar_siswa')
    else:
        form = SiswaForm()
    
    return render(request, 'siswa/tambah_siswa.html', {'form': form})

def detail_siswa(request, nisn):
    siswa = get_object_or_404(Siswa, nisn=nisn)
    return render(request, 'siswa/detail_siswa.html', {'siswa': siswa})

def edit_siswa(request, nisn):
    siswa = get_object_or_404(Siswa, nisn=nisn)
    if request.method == 'POST':
        form = SiswaForm(request.POST, instance=siswa)
        if form.is_valid():
            form.save()
            return redirect('siswa:daftar_siswa')
    else:
        form = SiswaForm(instance=siswa)
    
    return render(request, 'siswa/edit_siswa.html', {'form': form, 'siswa': siswa})

def hapus_siswa(request, nisn):
    siswa = get_object_or_404(Siswa, nisn=nisn)
    siswa.delete()
    return redirect('siswa:daftar_siswa')
