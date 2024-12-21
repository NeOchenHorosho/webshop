from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def logout_view(request):
    logout(request)
    return redirect('/')