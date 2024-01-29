from django.urls import path
from . import views

app_name = 'siswa'

urlpatterns = [
    path('', views.daftar_siswa, name='daftar_siswa'),
    path('tambah/', views.tambah_siswa, name='tambah_siswa'),
    path('<str:nisn>/', views.detail_siswa, name='detail_siswa'),
    path('<str:nisn>/edit/', views.edit_siswa, name='edit_siswa'),
    path('<str:nisn>/hapus/', views.hapus_siswa, name='hapus_siswa'),
]
