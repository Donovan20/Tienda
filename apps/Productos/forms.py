from django import forms #Se importan los formularios
from apps.Productos.models import Categoria, Producto, Venta #Se importan los modelos que se utilizaran

##Creacion del formulario Producto
class ProductoForm(forms.ModelForm):
    
    class Meta():
        model = Producto

        fields = [
            'nombreProducto',
            'descripcion',
            'costo',
            'existencia',
            'categoria'
        ]

        labels = {
            'nombreProducto': 'Nombre del Producto', 
            'descripcion': 'Descripcion',
            'costo' : 'Costo',
            'existencia': 'Existencia',
            'categoria' : 'Categoria(id de la Categoria)',
        }

        widgets = {
            'nombreProducto':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'costo':forms.TextInput(attrs={'class': 'form-control'}),
            'existencia':forms.TextInput(attrs={'class': 'form-control'}),
            'categoria':forms.TextInput(attrs={'class': 'form-control'}),
        }

##Creacion del formulario Categoria
class CategoriaForm(forms.ModelForm):
    class Meta():
                model= Categoria

                fields = [
                    'nombreCat',
                ]

                labels = {
                    'nombreCat': 'Nombre de la Categoria', 
                }

                widgets = {
                    'nombreCat' :forms.TextInput(attrs={'class': 'form-control'}),

                }
                
class VentaForm(forms.ModelForm):
    class Meta():
        model = Venta

        fields = [
            'nombreProducto',
            'descripcion',
            'costo',
            'cantidad',
            'total',
        ]

        labels = {
            'nombreProducto': 'Nombre del Producto', 
            'descripcion': 'Descripcion',
            'costo' : 'Costo',
            'cantidad': 'Cantidad',
            'total': 'Total',
        }

        widgets = {
            'nombreProducto':forms.TextInput(attrs={'class': 'form-control' ,'readonly':'True'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control' ,'readonly':'True'}),
            'costo':forms.NumberInput(attrs={'class': 'form-control' ,'readonly':'True'}),
            'cantidad':forms.NumberInput(attrs={'class': 'form-control'}),
            'total':forms.NumberInput(attrs={'class': 'form-control' ,'readonly':'True'}),
        }