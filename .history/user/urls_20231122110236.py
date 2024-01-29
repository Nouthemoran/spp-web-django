from django.urls import path
from . import views


app_name = 'user'  # nama aplkasi


urlpatterns = [
    path('', views.user_list, name='read'),
    path('create/', views.create_user, name='create'),
    path('update/<str:id_user>/', views.update_user, name='update'),
    path('delete/<str:id_user>/', views.delete_user, name='delete'),
 

]