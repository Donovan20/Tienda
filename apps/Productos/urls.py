from django.urls import path
from apps.Productos.views import index,producto,categoria,refrescos,viewCategorias, nuevoProducto, nuevaCategoria, editarProducto, editarCategoria, eliminarProducto, eliminarCategoria, venta, comprarProducto, pagar

urlpatterns = [
    path('', index),
    path('index', index, name="vistaIndex"),
    path('producto/',producto, name="vistaProductos"),
    path('categoria/',categoria, name="vistaCategorias"),
    path('venta/',venta,name ="vistaVentas"),
    path('refrescos',refrescos),
    path('ordenadas',viewCategorias.as_view()),
    path('nuevoProducto', nuevoProducto, name="nuevoProducto"),
    path('nuevaCategoria', nuevaCategoria, name="nuevaCategoria"),
    path('editarProducto/<idProducto>',editarProducto, name="editarProducto"),
    path('comprarProducto/<idProducto>',comprarProducto, name="comprarProducto"),
    path('pagar/',pagar, name="pagar"),
    path('editarCategoria/<idCategoria>',editarCategoria, name="editarCategoria"),
    path('eliminarProducto/<idProducto>',eliminarProducto, name="eliminarProducto"),
    path('eliminarCategoria/<idCategoria>',eliminarCategoria, name="eliminarCategoria")
]