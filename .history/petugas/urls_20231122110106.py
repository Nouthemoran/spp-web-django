from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_petugas, name='daftar_petugas'),
    path('create/', views.tambah_petugas, name='tambah_petugas'),
    path('<int:petugas_id>/', views.detail_petugas, name='detail_petugas'),
    path('<int:petugas_id>/edit/', views.edit_petugas, name='edit_petugas'),
    path('<int:petugas_id>/hapus/', views.hapus_petugas, name='hapus_petugas'),
]
