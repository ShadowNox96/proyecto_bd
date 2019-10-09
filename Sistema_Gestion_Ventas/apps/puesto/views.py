from django.shortcuts import render, redirect
from apps.puesto.models import Puesto
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.puesto.forms import PuestoForm
from django.urls import reverse_lazy
# Create your views here.

#Vista principal al entrar a puesto url ya configurada

#VIstas basadas en clases
class PuestoView(ListView):
    model = Puesto
    template_name = 'puesto/index.html'

class CrearPuesto(CreateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'puesto/crear-puesto.html'
    success_url = reverse_lazy('puesto')

class EditarPuesto(UpdateView):
    model = Puesto
    form_class = PuestoForm
    template_name = 'puesto/crear-puesto.html'
    success_url = reverse_lazy('puesto')
    
class EliminarPuesto(DeleteView):
    model = Puesto
    template_name = 'puesto/eliminar-puesto.html'
    success_url = reverse_lazy('puesto')

#modelos basados en funciones, aca abajo tira error el modelo Puesto, nose aun por que.
def editarPuesto(request, id_puesto):
    puesto= Puesto.objects.get(id_puesto=id_puesto)
    if request.method == 'GET':
        form = PuestoForm(instance=puesto)
    else:
        form = PuestoForm(request.POST, instance=puesto)
        if form.is_valid():
            form.save()
        return redirect('puesto')
    return render(request, 'puesto/crear-puesto.html',{'form':form})

#eliminar un registro
def eliminarPuesto(request, id_puesto):
    puesto = Puesto.objects.get(id_puesto=id_puesto)
    if request.method == 'POST':
        puesto.delete()
        #aca en este redirect va el nombre de la url que le damos en el archivo urls.py de la aplicaion
        return redirect('puesto')
    return render(request, 'puesto/eliminar-puesto.html', {'puesto': puesto})
