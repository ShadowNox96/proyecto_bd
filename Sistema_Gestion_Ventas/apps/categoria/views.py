from django.shortcuts import render, redirect
from apps.categoria.models import Categoria
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.categoria.forms import CategoriaForm
from django.urls import reverse_lazy
# Create your views here.

#Vista principal al entrar a puesto url ya configurada

#VIstas basadas en clases
class CategoriaViwe(ListView):
    model = Categoria
    template_name = 'categoria/index.html'

class CrearCategoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear-categoria.html'
    success_url = reverse_lazy('categoria')

class EditarCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear-categoria.html'
    success_url = reverse_lazy('categoria')
    
class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'categoria/eliminar-categoria.html'
    success_url = reverse_lazy('categoria')
