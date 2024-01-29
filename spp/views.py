from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import SPP
from .forms import SPPForm  # Import form yang telah dibuat

def daftar_spp(request):
    spp_list = SPP.objects.all()
    return render(request, 'spp/daftar_spp.html', {'spp_list': spp_list})

def tambah_spp(request):
    if request.method == 'POST':
        form = SPPForm(request.POST)
        if form.is_valid():
            # Mendapatkan nilai id_spp dari form atau request
            id_spp = request.POST.get('id_spp')
            tahun = form.cleaned_data['tahun']
            nominal = form.cleaned_data['nominal']
            
            # Membuat objek SPP dengan id_spp yang diberikan
            spp = SPP(id_spp=id_spp, tahun=tahun, nominal=nominal)
            spp.save()
            return HttpResponseRedirect('/spp/')
    else:
        form = SPPForm()
    
    return render(request, 'spp/tambah_spp.html', {'form': form})


def detail_spp(request, spp_id):
    spp = get_object_or_404(SPP, pk=spp_id)
    return render(request, 'spp/detail_spp.html', {'spp': spp})

def edit_spp(request, spp_id):
    spp = get_object_or_404(SPP, pk=spp_id)
    if request.method == 'POST':
        form = SPPForm(request.POST, instance=spp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/spp/')
    else:
        form = SPPForm(instance=spp)
    
    return render(request, 'spp/edit_spp.html', {'form': form, 'spp': spp})

def hapus_spp(request, spp_id):
    spp = get_object_or_404(SPP, pk=spp_id)
    spp.delete()
    return HttpResponseRedirect('/spp/')
