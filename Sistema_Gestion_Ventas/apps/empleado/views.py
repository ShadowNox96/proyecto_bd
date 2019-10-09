from django.shortcuts import render, redirect
from apps.empleado.models import Empleado
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.empleado.forms import  EmpleadoForm
from django.urls import reverse_lazy

class EmpleadoView(ListView):
    model = Empleado
    template_name = 'empleado/index.html'

class CrearEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear-empleado.html'
    success_url = reverse_lazy('empleado')

class EditarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear-empleado.html'
    success_url = reverse_lazy('empleado')
    
class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'empleado/eliminar-empleado.html'
    success_url = reverse_lazy('empleado')