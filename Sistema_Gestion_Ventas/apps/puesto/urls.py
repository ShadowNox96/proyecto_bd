from django.urls import path
from apps.puesto.views import  PuestoView, CrearPuesto, editarPuesto, eliminarPuesto, EditarPuesto, EliminarPuesto
urlpatterns = [
    path('', PuestoView.as_view(), name='puesto'),
    path('/crear', CrearPuesto.as_view() , name='crearpuesto'),
    #Aca en esta vista basada en funcion pide el parametro id_de puesto, pero cuando son vistaas basadas en clase pide el parametro por defecto pk que es la prymarykey
    #path('/editar/<id_puesto>', editarPuesto , name='editarpuesto'),
    path('/editar/<pk>', EditarPuesto.as_view() , name='editarpuesto'),
    #path('/eliminar/<id_puesto>', eliminarPuesto , name='eliminarpuesto'),
    path('/eliminar/<pk>', EliminarPuesto.as_view() , name='eliminarpuesto'),
]