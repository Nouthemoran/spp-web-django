from django.urls import path
from . import views

app_name = 'kelas'

urlpatterns = [
    path('', views.daftar_kelas, name='daftar_kelas'),
    path('tambah/', views.tambah_kelas, name='tambah_kelas'),
    path('<int:kelas_id>/', views.detail_kelas, name='detail_kelas'),
    path('<int:kelas_id>/edit/', views.edit_kelas, name='edit_kelas'),
    path('<int:kelas_id>/hapus/', views.hapus_kelas, name='hapus_kelas'),
]
