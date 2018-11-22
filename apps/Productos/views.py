from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Productos.models import Categoria,Producto,Venta
from django.views.generic import ListView
from apps.Productos.forms import ProductoForm, CategoriaForm, VentaForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def categoria(request):
	contexto = { 
		'categorias': Categoria.objects.all()
	}
	return render(request, 'categoria/categoria.html', contexto)

def producto(request):
	contexto = { 
		'productos': Producto.objects.all()
	}
	return render(request, 'producto/producto.html', contexto)

def index(request):
    return render(request,'base/index.html')

def refrescos(request):
    refrescos = { 
		'productos': Producto.objects.all()
	}
    return render(request,'producto/refrescos.html',refrescos)
def venta(request):
    carrito = { 
		'productos': Venta.objects.all(),
        'total': sumarTodo()
	}
    return render(request,'venta/venta.html',carrito)

class viewCategorias(ListView):
    queryset= Categoria.objects.order_by('nombreCat')
    template_name='categoria/ordenadas.html'

def nuevoProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vistaProductos')
    else:
        form = ProductoForm()
    return render(request, 'producto/productoFormulario.html', {'form' : form})

def nuevaCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vistaCategorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/categoriaFormulario.html', {'form' : form})

def editarProducto(request,idProducto):
    producto = Producto.objects.get(id=idProducto)
    if(request.method == 'GET'):
        form = ProductoForm(instance = producto)
    else:
        form = ProductoForm(request.POST, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('vistaProductos')   
    return render(request, 'producto/productoFormulario.html', {'form' : form})

def comprarProducto(request,idProducto):
    
    producto = Producto.objects.get(id=idProducto)
    producto2 = Producto.objects.filter(pk=idProducto).first()
    if(request.method == 'GET'):
        form = VentaForm(instance = producto)
    else:
        
        form2= VentaForm(request.POST)
        if form2.is_valid():
            if(producto.existencia >= int(request.POST['cantidad'])):
                actualizado = producto.existencia - int(request.POST['cantidad'])
                producto2.existencia = actualizado
                total = int(producto.costo) * int(request.POST['cantidad']);
                prueba = form2.save(commit=False)
                prueba.total = total;
                prueba.save()
                producto2.save()
                messages.success(request, 'Agregado al carrito!')
            elif(producto.existencia <int(request.POST['cantidad'])):
                messages.error(request, 'No alcanzas a comprar los productos!')
                
        return redirect('vistaVentas')   
    return render(request, 'producto/productoCompra.html', {'form' : form})


def sumarTodo():
    suma = Venta.objects.all()
    total = 0
    for datos in suma:
        total = total + datos.total
    return total


def editarCategoria(request,idCategoria):
    categoria = Categoria.objects.get(id=idCategoria)
    if(request.method == 'GET'):
        form = CategoriaForm(instance = categoria)
    else:
        form = CategoriaForm(request.POST, instance = categoria)
        if form.is_valid():
            form.save()
        return redirect('vistaCategorias')   
    return render(request, 'categoria/categoriaFormulario.html', {'form' : form})

def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    if(request.method == 'GET'):
        instance = producto
        instance.delete()
    return redirect('vistaProductos') 

def eliminarCategoria(request, idCategoria):
    categoria = Categoria.objects.get(id=idCategoria)
    if(request.method == 'GET'):
        instance = categoria
        instance.delete()
    return redirect('vistaCategorias')

def pagar(request):
    ventas = Venta.objects.all()
    if(request.method == 'GET'):
        instance = ventas
        instance.delete()
        messages.success(request, 'Compra realizada!')
    return redirect('vistaProductos')