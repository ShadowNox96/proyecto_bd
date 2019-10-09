from django.urls import path
from apps.producto.views import CrearProducto, ProductoView, EditarProducto, EliminarProducto

urlpatterns =[
    path('', ProductoView.as_view(), name='producto'),
    path('/crear', CrearProducto.as_view(), name='crearproducto'),
    path('/editar/<pk>', EditarProducto.as_view(), name='editarproducto'),
    path('/eliminar/<pk>', EliminarProducto.as_view(), name='eliminarproducto'),
]