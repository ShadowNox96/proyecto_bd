from django.urls import path
from apps.categoria.views import CategoriaViwe, CrearCategoria, EditarCategoria, EliminarCategoria
urlpatterns = [
    path('', CategoriaViwe.as_view(), name='categoria'),
    path('/crear', CrearCategoria.as_view() , name='crearcategoria'),
    #Aca en esta vista basada en funcion pide el parametro id_de puesto, pero cuando son vistaas basadas en clase pide el parametro por defecto pk que es la prymarykey
    #path('/editar/<id_puesto>', editarPuesto , name='editarpuesto'),
    path('/editar/<pk>', EditarCategoria.as_view() , name='editarcat'),
    #path('/eliminar/<id_puesto>', eliminarPuesto , name='eliminarpuesto'),
    path('/eliminar/<pk>', EliminarCategoria.as_view() , name='eliminarcat'),
]