from django.urls import path
from . import views


app_name = 'pembayaran'

urlpatterns = [
    path('', views.daftar_pembayaran, name='daftar_pembayaran'),
    path('tambah/', views.tambah_pembayaran, name='tambah_pembayaran'),
    path('cetak/<int:pembayaran_id>/', views.cetak_pembayaran, name='cetak_pembayaran'),
    path('<int:pembayaran_id>/', views.detail_pembayaran, name='detail_pembayaran'),
    path('<int:pembayaran_id>/edit/', views.edit_pembayaran, name='edit_pembayaran'),
    path('<int:pembayaran_id>/hapus/', views.hapus_pembayaran, name='hapus_pembayaran'),

]
