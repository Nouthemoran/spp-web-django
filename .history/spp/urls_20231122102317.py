from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_spp, name='daftar_spp'),
    path('tambah/', views.tambah_spp, name='tambah_spp'),
    path('spp/<int:spp_id>/', views.detail_spp, name='detail_spp'),
    path('<int:spp_id>/edit/', views.edit_spp, name='edit_spp'),
    path('<int:spp_id>/hapus/', views.hapus_spp, name='hapus_spp'),
]
