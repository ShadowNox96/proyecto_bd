from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from apps.producto.models import Producto
from apps.producto.forms import ProductoForm

# Create your views here.
class ProductoView(ListView):
    model = Producto
    template_name = 'producto/index.html'

class CrearProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear-producto.html'
    success_url = reverse_lazy('producto')

class EditarProducto(UpdateView):
    model = Producto
    form_class= ProductoForm
    template_name = 'producto/crear-producto.html'
    success_url = reverse_lazy('producto')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'producto/eliminar-producto.html'
    success_url = reverse_lazy('producto')