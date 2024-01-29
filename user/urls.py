from django.urls import path

# import class View
from .views import CustomLoginView,CustomLogoutView,RegisterView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user/logout/', CustomLogoutView.as_view(), name='user_logout'),
    path('register/', RegisterView.as_view(), name='register')
]