from django.urls import path
from . import views

app_name = 'history_pembayaran'

urlpatterns = [
    path('', views.history_pembayaran, name='history_pembayaran'),
]
