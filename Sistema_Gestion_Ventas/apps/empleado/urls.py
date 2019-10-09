from django.urls import path
from apps.empleado.views import EmpleadoView, EliminarEmpleado, EditarEmpleado, CrearEmpleado
urlpatterns = [
    path('', EmpleadoView.as_view(), name='empleado'),
    path('/crear', CrearEmpleado.as_view() , name='crearempleado'),
    #Aca en esta vista basada en funcion pide el parametro id_de puesto, pero cuando son vistaas basadas en clase pide el parametro por defecto pk que es la prymarykey
    #path('/editar/<id_puesto>', editarPuesto , name='editarpuesto'),
    path('/editar/<pk>', EditarEmpleado.as_view() , name='editarempleado'),
    #path('/eliminar/<id_puesto>', eliminarPuesto , name='eliminarpuesto'),
    path('/eliminar/<pk>', EliminarEmpleado.as_view() , name='eliminarempleado'),
]