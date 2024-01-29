from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import  ,LoginView,LogoutView

class CustomLoginView(LoginView):
	template_name = 'user/login.html'
	redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'user/login.html'
    next_page = 'login'

class CustomRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')  # Redirect ke halaman login setelah registrasi berhasil
