from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class ProductList(ListView):
    model = models.Product
    template_name = 'home.html'